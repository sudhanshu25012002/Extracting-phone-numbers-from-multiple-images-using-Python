import os
import re
import easyocr

# Function to check if a phone number is in the format of an Indian phone number
def is_indian_phone_number(phone_number):
    # Regular expression pattern for Indian phone numbers
    pattern = r'^(\+91\s\d{5}\s\d{5}|\+91\s\d{4}\s\d{3}\s\d{3}|\+91\s\d{10})$'
    return re.match(pattern, phone_number) is not None

# Path to the image file
image_path = 'image/whatstapp test image.jpg'  # Adjust the path as needed
output_file = 'detected_phone_numbers.txt'  # Name of the output text file

# Check if the image file exists
if not os.path.isfile(image_path):
    print("Image file not found.")
    exit()

# Initialize the OCR reader
reader = easyocr.Reader(['en'])

# Perform OCR on the image
result = reader.readtext(image_path)

# Extract phone numbers from the OCR result
phone_numbers = []
for detection in result:
    text = detection[1]
    # Check if the detected text matches a phone number pattern and is in the format of an Indian phone number
    if any(char.isdigit() for char in text) and any(char.isdigit() for char in text.replace('+', '')):
        if is_indian_phone_number(text):
            phone_numbers.append(text)

# Write the detected Indian phone numbers to the output text file
if phone_numbers:
    mode = 'a' if os.path.exists(output_file) else 'w'
    with open(output_file, mode) as file:
        if mode == 'w':
            file.write("Detected Indian phone number(s):\n")
        for number in phone_numbers:
            file.write(number + '\n')
    print(f"Detected Indian phone numbers have been saved to '{output_file}'.")
else:
    print("No Indian phone numbers found in the image.")
