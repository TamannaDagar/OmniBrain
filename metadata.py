import fitz
import json
import os

# Path of the PDF file
pdf_path = "data/sample.pdf"

try:
    # Open the PDF
    document = fitz.open(pdf_path)

    # Extract metadata
    metadata = document.metadata

    # Create a dictionary
    pdf_metadata = {
        "file_name": os.path.basename(pdf_path),
        "title": metadata.get("title"),
        "author": metadata.get("author"),
        "subject": metadata.get("subject"),
        "creator": metadata.get("creator"),
        "producer": metadata.get("producer"),
        "creation_date": metadata.get("creationDate"),
        "modification_date": metadata.get("modDate"),
        "total_pages": len(document)
    }

    # Print metadata
    print(json.dumps(pdf_metadata, indent=4))

    # Create output folder if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Save metadata as JSON
    with open("output/metadata.json", "w") as file:
        json.dump(pdf_metadata, file, indent=4)

    print("\nMetadata extraction completed successfully!")

except FileNotFoundError:
    print("PDF file not found.")

except Exception as error:
    print("Error:", error)