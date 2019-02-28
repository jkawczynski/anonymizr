from dataclasses import dataclass
from typing import List

from PIL import Image
from pytesseract import image_to_string, image_to_boxes, Output

from anonymizr.emails import is_email_address


@dataclass(order=True)
class ImageWord:
    word: str
    start_word_coordinates: tuple
    end_word_coordinates: tuple

    @property
    def is_email(self):
        return is_email_address(self.word)


class TesseractImage:
    def __init__(self, image_path):
        self.image_path = image_path
        self._raw_text = None
        self.words = []
        self.image_text = None
        self.image_boxes = None
        self.processed = False

    def process_image(self):
        self._raw_text = image_to_string(Image.open(self.image_path))
        self.image_boxes = image_to_boxes(
            Image.open(self.image_path), output_type=Output.DICT
        )
        self.words = [
            word
            for word in self._raw_text.replace("\n", " ").split(" ")
            if word.strip()
        ]
        self.image_text = self._raw_text.replace(" ", "").replace("\n", "")

    def process_if_needed(self):
        if self.processed:
            return

        self.process_image()

    def get_words_and_positions(self) -> List[ImageWord]:
        self.process_if_needed()

        result = []
        for word in self.words:
            l_index = self.image_text.index(word)
            r_index = l_index + len(word)
            start_coordinates = (
                self.image_boxes["top"][l_index],
                self.image_boxes["right"][l_index],
                self.image_boxes["bottom"][l_index],
                self.image_boxes["left"][l_index],
            )
            end_coordinates = (
                self.image_boxes["top"][r_index - 1],
                self.image_boxes["right"][r_index - 1],
                self.image_boxes["bottom"][r_index - 1],
                self.image_boxes["left"][r_index - 1],
            )
            result.append(ImageWord(word, start_coordinates, end_coordinates))

        return result
