from PIL import Image
from PIL.ExifTags import TAGS

import pillow_heif


def convert_heic_to_jpeg(image_path):
    heic_file = pyheif.read(image_path)

def get_photo_date_taken(image_path):
    image = Image.open(image_path)

    exif_data = image.getexif()

    if exif_data is not None:
        for tag, value in exif_data.items():
            if TAGS.get(tag) == 'DateTime':
                return value
    else:
        return None


def is_image_file(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except (IOError, OSError):
        return False

