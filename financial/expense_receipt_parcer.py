import pytesseract
from PIL import Image
import re
import json
import os

def extract_text_from_image(image_path):
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return text
    except Exception as e:
        print(f" Error reading image: {e}")
        return ""

def parse_receipt_text(text):
    data = {}

 
    date_match = re.search(r'(\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})', text)
    total_match = re.search(r'Total\s*[:\-]?\s*₹?\s?(\d+[.,]?\d*)', text, re.IGNORECASE)
    vendor_match = re.search(r'^(.*?)(\n|$)', text.strip())  # first line = vendor name

    data['vendor'] = vendor_match.group(1).strip() if vendor_match else "Unknown"
    data['date'] = date_match.group(1) if date_match else "Not Found"
    data['total'] = float(total_match.group(1).replace(",", "")) if total_match else 0.0
    data['raw_text'] = text

    return data

def main():
    print(" Expense Receipt Parser CLI")
    print("-" * 30)
    image_path = input("Enter receipt image path (JPG/PNG): ").strip()

    if not os.path.exists(image_path):
        print(" File does not exist.")
        return

    text = extract_text_from_image(image_path)
    if not text:
        print(" No text extracted.")
        return

    parsed_data = parse_receipt_text(text)

    print("\n Parsed Receipt Data")
    print(json.dumps(parsed_data, indent=2))

    save = input("\nSave output to JSON file? (y/n): ").lower()
    if save == 'y':
        with open("parsed_receipt.json", "w") as f:
            json.dump(parsed_data, f, indent=2)
        print(" Data saved to parsed_receipt.json")

if __name__ == "__main__":
    main()
