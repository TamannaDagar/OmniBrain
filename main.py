import os

print("=" * 50)
print("      PDF Processing Pipeline Started")
print("=" * 50)

scripts = [
    "metadata.py",
    "text_extraction.py",
    "D4_image_extraction.py",      
    "json_generator.py",
    "page_wise_processing.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    status = os.system(f"python {script}")

    if status == 0:
        print(f"{script} completed successfully.")
    else:
        print(f"Error while running {script}")

print("\n" + "=" * 50)
print("PDF Processing Pipeline Completed Successfully!")
print("=" * 50)