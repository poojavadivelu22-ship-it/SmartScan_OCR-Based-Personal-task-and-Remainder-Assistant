import pytesseract
from PIL import Image
import shutil

tesseract_path = shutil.which("tesseract")

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path


def extract_text(image_file):
    image = Image.open(image_file).convert("RGB")

    text = pytesseract.image_to_string(
        image,
        config="--psm 6"
    )

    return text.strip()
