import os
import argparse
from datetime import datetime

def rename_images(folder_path):
    """Rename image files in the given folder based on creation date."""
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Get creation time
            creation_time = os.path.getctime(file_path)
            date_str = datetime.fromtimestamp(creation_time).strftime("%Y%m%d_%H%M%S")
            
            # Keep original extension
            extension = os.path.splitext(filename)[1]
            new_name = f"{date_str}{extension}"
            new_path = os.path.join(folder_path, new_name)

            # Avoid overwriting files
            counter = 1
            while os.path.exists(new_path):
                new_name = f"{date_str}_{counter}{extension}"
                new_path = os.path.join(folder_path, new_name)
                counter += 1

            os.rename(file_path, new_path)
            print(f"Renamed: {filename} → {new_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk rename images based on creation date.")
    parser.add_argument("folder", help="Path to the folder containing images")
    args = parser.parse_args()

    rename_images(args.folder)
