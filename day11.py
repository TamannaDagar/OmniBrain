import fitz
import json
import os


def extract_metadata(doc):
    metadata = doc.metadata

    pdf_metadata = {
        "title": metadata.get("title"),
        "author": metadata.get("author"),
        "subject": metadata.get("subject"),
        "creator": metadata.get("creator"),
        "producer": metadata.get("producer"),
        "creation_date": metadata.get("creationDate"),
        "modification_date": metadata.get("modDate"),
        "pages": len(doc)
    }

    return pdf_metadata


def extract_text(doc):
    pages = []

    for page_number in range(len(doc)):
        page = doc.load_page(page_number)

        pages.append({
            "page_number": page_number + 1,
            "text": page.get_text()
        })

        print(f"Page {page_number + 1} Extracted")

    return pages


def save_json(data):
    os.makedirs("output", exist_ok=True)

    with open("output/output.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("JSON Saved Successfully")


def main():
    pdf_path = "data/sample.pdf"

    try:
        print("Opening PDF...")

        doc = fitz.open(pdf_path)

        metadata = extract_metadata(doc)

        pages = extract_text(doc)

        result = {
            "status": True,
            "file_name": os.path.basename(pdf_path),
            "metadata": metadata,
            "pages": pages
        }

        save_json(result)

        doc.close()

        print("Process Completed Successfully")

    except Exception as e:
        print("Error :", e)


if __name__ == "__main__":
    main()