import easyocr
import numpy as np
from PIL import Image


# Create OCR reader
reader = easyocr.Reader(["en"])


def extract_text(image_file):

    image = Image.open(image_file).convert("RGB")

    image_array = np.array(image)

    results = reader.readtext(image_array)

    extracted_text = []

    for result in results:
        text = result[1]
        extracted_text.append(text)

    return "\n".join(extracted_text)