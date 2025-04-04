# photo_organizer.py
import argparse
import os

from photo_organizer import get_photo_date_taken
from photo_organizer import is_image_file



def main():
    parser = argparse.ArgumentParser(description="This script organizes photos by eliminating duplicates :D")

    parser.add_argument("--input-dir", "-i", help="Directory where the photos are located.")
    parser.add_argument("--output-dir", "-o", help="Directory where the organized photos will be moved to.")

    args = parser.parse_args()

    input_directory = args.input_dir
    output_directory = args.output_dir

    print(f"Input directory: {input_directory}")
    print(f"Output directory: {output_directory}")

    photos = {}
    total_images = 0
    total_files = 0

    for root, dirs, files in os.walk(args.input_dir):
        total_files += len(files)
        
        for file in files:
            current_file_full_path = os.path.join(root, file)

            is_image = is_image_file(current_file_full_path)
            
            if is_image:
                total_images += 1
            else:
                continue
            
            date = get_photo_date_taken(current_file_full_path)
            if file in photos:
                pass
            else:
                photos[file] = date

    unique_photos = len(photos)

    print(f"In total, {total_files} files were found.")
    print(f"Of those, {total_images} were images.")
    print(f"{unique_photos} of those photos were unique.")


if __name__ == "__main__":
    main()

