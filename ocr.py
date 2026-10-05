import easyocr
import numpy as np
import cv2
from PIL import Image

# Create OCR reader
reader = easyocr.Reader(["en"])


def extract_text(image_file):

    # Read image
    image = Image.open(image_file).convert("RGB")

    # Convert PIL image to NumPy
    image_array = np.array(image)

    # Convert RGB to grayscale
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

    # Improve image quality
    gray = cv2.resize(
        gray,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC
    )

    # Reduce noise
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # Improve contrast
    processed_image = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    # OCR
    results = reader.readtext(
        processed_image,
        detail=1,
        paragraph=False
    )

    # Extract text
    extracted_text = []

    for result in results:
        text = result[1].strip()

        if text:
            extracted_text.append(text)

    return "\n".join(extracted_text)
