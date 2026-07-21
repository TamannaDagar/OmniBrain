import fitz
import json
import os

pdf_path = "data/sample.pdf"

try:
    document = fitz.open(pdf_path)

    os.makedirs("output", exist_ok=True)

    extracted_text = {}

    with open("output/extracted_text.txt", "w", encoding="utf-8") as txt_file:

        for page_number in range(len(document)):

            page = document.load_page(page_number)

            text = page.get_text()

            txt_file.write(f"\n========== Page {page_number + 1} ==========\n")
            txt_file.write(text)

            extracted_text[f"Page_{page_number + 1}"] = text

    with open("output/extracted_text.json", "w", encoding="utf-8") as json_file:
        json.dump(extracted_text, json_file, indent=4, ensure_ascii=False)

    print("Text extraction completed successfully!")

except FileNotFoundError:
    print("PDF file not found.")

except Exception as error:
    print("Error:", error)