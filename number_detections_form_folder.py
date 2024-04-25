import os
import re
import easyocr

# Function to check if a phone number is in the format of an Indian phone number
def is_indian_phone_number(phone_number):
    # Regular expression pattern for Indian phone numbers
    pattern = r'^(\+91\s\d{5}\s\d{5}|\+91\s\d{4}\s\d{3}\s\d{3}|\+91\s\d{10})$'
    return re.match(pattern, phone_number) is not None

# Path to the folder containing images
folder_path = 'image'  # Adjust the path as needed
output_file = 'detected_phone_numbers.txt'  # Name of the output text file

# Check if the folder exists
if not os.path.isdir(folder_path):
    print("Image folder not found.")
    exit()

# Initialize the OCR reader
reader = easyocr.Reader(['en'])

# List to store detected phone numbers
detected_phone_numbers = []

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Process only image files
        image_path = os.path.join(folder_path, filename)
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
        if phone_numbers:
            detected_phone_numbers.extend(phone_numbers)

# Print the names of the images scanned
if detected_phone_numbers:
    print("Images scanned:")
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Process only image files
            print(filename)

# Write the detected Indian phone numbers to the output text file
if detected_phone_numbers:
    mode = 'a' if os.path.exists(output_file) else 'w'
    with open(output_file, mode) as file:
        for number in detected_phone_numbers:
            file.write(number + '\n')
    print(f"Detected Indian phone numbers from images in the folder '{folder_path}' have been saved to '{output_file}'.")
else:
    print("No Indian phone numbers found in the images in the folder.")
