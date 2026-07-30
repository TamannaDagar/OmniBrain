import fitz
import json
import os
import logging

# Create logs folder
os.makedirs("logs", exist_ok=True)

# Logging Configuration
logging.basicConfig(
    filename="logs/pdf.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def extract_metadata(doc):
    metadata = doc.metadata

    return {
        "title": metadata.get("title"),
        "author": metadata.get("author"),
        "subject": metadata.get("subject"),
        "creator": metadata.get("creator"),
        "producer": metadata.get("producer"),
        "creation_date": metadata.get("creationDate"),
        "modification_date": metadata.get("modDate"),
        "pages": len(doc)
    }


def extract_text(doc):
    pages = []

    for page_number in range(len(doc)):
        page = doc.load_page(page_number)

        pages.append({
            "page_number": page_number + 1,
            "text": page.get_text()
        })

        logging.info(f"Page {page_number + 1} Extracted")

    return pages


def save_json(data):
    os.makedirs("output", exist_ok=True)

    with open("output/output.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    logging.info("JSON Saved Successfully")


def main():

    pdf_path = "data/sample.pdf"

    try:

        logging.info("Program Started")

        doc = fitz.open(pdf_path)

        logging.info("PDF Opened Successfully")

        metadata = extract_metadata(doc)

        logging.info("Metadata Extracted")

        pages = extract_text(doc)

        result = {
            "status": True,
            "file_name": os.path.basename(pdf_path),
            "metadata": metadata,
            "pages": pages
        }

        save_json(result)

        doc.close()

        logging.info("Program Finished Successfully")

        print("Completed Successfully")

    except Exception as e:

        logging.error(str(e))

        print("Error :", e)


if __name__ == "__main__":
    main()