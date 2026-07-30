import fitz
import json
import os


def test_pdf_exists(pdf_path):
    if os.path.exists(pdf_path):
        print("Test 1 Passed : PDF File Found")
        return True
    else:
        print("Test 1 Failed : PDF File Not Found")
        return False


def test_open_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        print("Test 2 Passed : PDF Opened Successfully")
        doc.close()
        return True
    except Exception:
        print("Test 2 Failed : Unable to Open PDF")
        return False


def test_metadata(pdf_path):
    try:
        doc = fitz.open(pdf_path)

        metadata = doc.metadata

        print("Test 3 Passed : Metadata Extracted")

        doc.close()

        return metadata

    except Exception:
        print("Test 3 Failed")
        return None


def test_text_extraction(pdf_path):
    try:

        doc = fitz.open(pdf_path)

        total_pages = len(doc)

        for page in doc:
            page.get_text()

        print(f"Test 4 Passed : Text Extracted from {total_pages} Pages")

        doc.close()

        return True

    except Exception:

        print("Test 4 Failed")

        return False


def test_json_creation():

    sample = {
        "status": True,
        "message": "Testing JSON"
    }

    os.makedirs("output", exist_ok=True)

    with open("output/test.json", "w") as file:
        json.dump(sample, file, indent=4)

    if os.path.exists("output/test.json"):
        print("Test 5 Passed : JSON Created")
    else:
        print("Test 5 Failed")


def main():

    pdf_path = "data/sample.pdf"

    print("\nRunning Unit Tests...\n")

    test_pdf_exists(pdf_path)

    test_open_pdf(pdf_path)

    test_metadata(pdf_path)

    test_text_extraction(pdf_path)

    test_json_creation()

    print("\nAll Tests Completed")


if __name__ == "__main__":
    main()