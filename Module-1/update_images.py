#!/usr/bin/env python3

import os
from PIL import Image

def convert_to_jpeg(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Iterate through each file in the source directory
    for filename in os.listdir(source_dir):
        # Get the full path of the current file
        source_path = os.path.join(source_dir, filename)

        # Check if the file is an image
        if not os.path.isfile(source_path) or filename == ".DS_Store":
            continue

        # Open the image file using Pillow
        image = Image.open(source_path)
        image = image.rotate(-90).resize((128,128))

        # Convert and save the image as JPEG format without extension
        destination_filename = os.path.splitext(filename)[0]
        destination_path = os.path.join(destination_dir, destination_filename)

        # Save the image as JPEG format
        image.convert("RGB").save(destination_path, "JPEG")

        # Close the image file
        image.close()

        print(f"Converted {filename} to JPEG.")

# Usage example
source_path = "/home/student-03-08110dd7f3ea/images/"
destination_path = "/opt/icons/"
convert_to_jpeg(source_path, destination_path)