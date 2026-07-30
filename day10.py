# Handle Password-Protected & Corrupted PDFs
import fitz

def open_pdf(path):
    try:
        doc = fitz.open(path)

        if doc.needs_pass:
            return {
                "status": False,
                "message": "Password protected PDF"
            }

        return doc

    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }