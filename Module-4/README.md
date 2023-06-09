# Automate Updating Catalog Information

You work for an online fruits store and need to develop a system to update the catalog information using data provided by your suppliers. The suppliers send two files: large images in .TIF format and descriptions in .txt format. Your task is to process this data and update the catalog on your company's online website.

## Requirements

1. **Image Processing:**
   - Convert the large images (in .TIF format) to smaller JPEG images.

2. **Description Processing:**
   - Turn the product descriptions (in .txt format) into HTML files.
   - The HTML files should display the respective image and product description.

3. **Upload to Web Service:**
   - Upload the contents of the HTML files to a web service that is already running using Django.
   - Use Python requests to upload the data to your Django server.

4. **Data Extraction:**
   - Extract the name and weight of all fruits from the .txt files.

5. **Supplier Notification:**
   - Once the task is complete, notify the supplier via email.
   - The email should indicate the total weight of fruit (in lbs) that was uploaded.
   - Attach a PDF to the email with the name of the fruit and its total weight (in lbs).

6. **System Health Check:**
   - In parallel with the automation process, check the health of the system.
   - If any issues are detected, send an email notification.

## Implementation

Create a Python script that performs the following tasks:

1. Process the images and descriptions received from the suppliers.
2. Update the online catalog with the new products.
3. Send an email to the supplier with the total weight of the uploaded fruit and a PDF attachment.
4. Continuously monitor the system's health and send email notifications if any issues occur.

## Getting Started

To get started with the script, follow these steps:

1. Clone this repository.
2. Install the required dependencies.
3. Run the Python script.

## Dependencies

Ensure you have the following dependencies installed:

- Python
- Django

## Usage

1. Place the image files (.TIF format) and description files (.txt format) in the designated input directory.
2. Run the Python script to process and update the catalog.
3. Check the output directory for the generated HTML files and uploaded data.
4. Monitor the system health and receive email notifications.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please submit a pull request.
