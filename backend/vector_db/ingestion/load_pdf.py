# import the libraries
import fitz
from pathlib import Path

BASE_DIR= Path(__file__).resolve().parent

def load_pdf(filename):
    pdf_path= BASE_DIR.parent /"data" / "pdfs" / filename

    document= fitz.open(pdf_path)

# extract the text of pdf
    text=""

    for page in document:       # loops through every page
        text += page.get_text()          # extracts all readable text from that page, combines all pages into one string

    document.close()

    return text

if __name__== "__main__":

    pdf_text= load_pdf('sample.pdf')


    print("Pdf Loaded successfully!")
    print(pdf_text[:1000])  # prints only first 1000 characters



