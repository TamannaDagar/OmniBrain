import fitz
import json
import os

pdf_path = "data/sample.pdf"

try:
    document = fitz.open(pdf_path)

    complete_data = {
        "file_name": os.path.basename(pdf_path),
        "total_pages": len(document),
        "metadata": document.metadata,
        "pages": []
    }

    for page_number in range(len(document)):
        page = document.load_page(page_number)

        page_data = {
            "page": page_number + 1,
            "text": page.get_text().strip()
        }

        complete_data["pages"].append(page_data)

    os.makedirs("output", exist_ok=True)

    with open("output/complete_pdf_data.json", "w", encoding="utf-8") as file:
        json.dump(complete_data, file, indent=4, ensure_ascii=False)

    print("Structured JSON generated successfully!")

except FileNotFoundError:
    print("PDF file not found.")

except Exception as e:
    print("Error:", e)