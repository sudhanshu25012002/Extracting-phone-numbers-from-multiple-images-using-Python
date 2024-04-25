from PIL import Image
import os
import pyperclip
import re
import send2trash
import pytesseract

# Path to the directory containing images
input_path = 'imgtotext/image/'

# Initialize list to store extracted text
all_text = []

# Loop through each image in the directory
for root, dirs, filenames in os.walk(input_path):
    for filename in filenames:
        try:
            # Open the image and extract text using pytesseract
            img = Image.open(os.path.join(root, filename))
            text = pytesseract.image_to_string(img)

            # Append extracted text to the list
            all_text.append(text.strip())

            # Move the processed image to the trash
            send2trash.send2trash(os.path.join(root, filename))
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue

# Regular expression to match phone numbers
phone_regex = re.compile(r'(\+?\d{0,3}\s?\d{5}\s?\d{5})')

# Extract phone numbers from the extracted text
matches = [match.group(0) for text in all_text for match in phone_regex.finditer(text)]

# Remove duplicate phone numbers
distinct_matches = list(set(matches))

if distinct_matches:
    # Copy unique phone numbers to clipboard
    pyperclip.copy('\n'.join(distinct_matches))
    print(f"{len(distinct_matches)} unique phone number(s) copied to clipboard.")
else:
    print('No phone numbers found.')

