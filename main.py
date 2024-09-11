import zipfile
import os

# Function to extract zip file
def extract_zip(file_path, extract_to):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    # Check if the file is a zip file
    if not zipfile.is_zipfile(file_path):
        print(f"{file_path} is not a valid zip file.")
        return

    # Extract the zip file
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Extracted all files to {extract_to}")

# Example usage
zip_file_path = r"F:\Python_Program to extract zipfile\ZipFiles\archive.zip"  # Replace with your zip file path
extract_directory = r"F:\Python_Program to extract zipfile\ExtractFiles"  # Replace with your desired extraction path
if __name__=="__main__":
 extract_zip(zip_file_path, extract_directory)
