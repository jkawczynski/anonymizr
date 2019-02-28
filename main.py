import os.path

from anonymizr.tesseract_utils import TesseractImage


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image = TesseractImage(os.path.join(BASE_DIR, "sample.png"))
image_word = image.get_words_and_positions()[0]

print(
    image_word.word, image_word.start_word_coordinates, image_word.end_word_coordinates
)
