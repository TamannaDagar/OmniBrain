import fitz
import json
import os

pdf_path = "data/sample.pdf"

try:
    # Open PDF
    document = fitz.open(pdf_path)

    page_data = []

    # Read every page
    for page_number in range(len(document)):

        page = document.load_page(page_number)

        text = page.get_text().strip()

        images = []

        image_list = page.get_images(full=True)

        for index, img in enumerate(image_list, start=1):
            images.append(f"page_{page_number + 1}_image_{index}.png")

        page_info = {
            "page_number": page_number + 1,
            "text": text,
            "total_images": len(images),
            "images": images
        }

        page_data.append(page_info)

    os.makedirs("output", exist_ok=True)

    with open("output/page_wise_data.json", "w", encoding="utf-8") as file:
        json.dump(page_data, file, indent=4, ensure_ascii=False)

    print("Page-wise JSON generated successfully!")

except FileNotFoundError:
    print("PDF file not found.")

except Exception as e:
    print("Error:", e)