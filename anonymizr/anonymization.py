from PIL import Image, ImageDraw

from anonymizr.tesseract_utils import ImageWord, TesseractImage


def draw_black_rectangle(image: TesseractImage, word: ImageWord) -> Image:
    """
    Draws rectangle on tesseract image for given word

    :param image: Input image
    :param word: Word to draw black rectangle over
    :return PIL image object - not yet saved
    """
    opened_image = Image.open(image.image_path).convert("RGB")
    draw = ImageDraw.Draw(opened_image)
    width, height = opened_image.size
    draw.rectangle(
        xy=(
            (word.start_word_coordinates[3], height - word.start_word_coordinates[2] + 5),
            (word.end_word_coordinates[1], height - word.end_word_coordinates[0] - 5)
        ),
        outline="black",
        fill="black",
    )
    return opened_image
