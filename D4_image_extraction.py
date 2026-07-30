import fitz
import os
import io
from PIL import Image

# PDF Path
pdf_path = "data/sample.pdf"

# Output Folder
output_folder = "output/images"

try:
    # Create output folder
    os.makedirs(output_folder, exist_ok=True)

    # Open PDF
    document = fitz.open(pdf_path)

    total_images = 0

    # Loop through all pages
    for page_number in range(len(document)):

        page = document.load_page(page_number)

        image_list = page.get_images(full=True)

        if not image_list:
            continue

        # Loop through all images on current page
        for image_index, img in enumerate(image_list, start=1):

            try:
                xref = img[0]

                # Extract image bytes
                base_image = document.extract_image(xref)
                image_bytes = base_image["image"]

                # Read image using Pillow
                image = Image.open(io.BytesIO(image_bytes))

                # Convert unsupported modes
                if image.mode in ("RGBA", "P"):
                    image = image.convert("RGB")

                # Save as PNG
                image_name = f"page_{page_number+1}_image_{image_index}.png"
                image_path = os.path.join(output_folder, image_name)

                image.save(image_path, "PNG")

                total_images += 1

                print(f"Saved: {image_name}")

            except Exception:

                # If PNG conversion fails, save as JPEG
                try:
                    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

                    image_name = f"page_{page_number+1}_image_{image_index}.jpg"
                    image_path = os.path.join(output_folder, image_name)

                    image.save(image_path, "JPEG", quality=95)

                    total_images += 1

                    print(f"Saved: {image_name}")

                except Exception as e:
                    print(f"Failed to extract image on Page {page_number+1}: {e}")

    print("\n--------------------------------")
    print(f"Total Images Extracted : {total_images}")
    print(f"Saved Location         : {output_folder}")
    print("--------------------------------")

except FileNotFoundError:
    print("Error: PDF file not found.")

except Exception as e:
    print("Unexpected Error:", e)