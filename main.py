import os.path

from anonymizr.anonymization import draw_black_rectangle
from anonymizr.emails import is_email_address
from anonymizr.tesseract_utils import TesseractImage


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image = TesseractImage(os.path.join(BASE_DIR, "sample.png"))
image_words = image.get_words_and_positions()

emails = [
    image_word for image_word in image_words
    if is_email_address(image_word.word)
]

for email in emails:
    draw_black_rectangle(image, email)
