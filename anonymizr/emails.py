"""Email processing module"""
import re


EMAIL_REGEX = re.compile(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}")


def is_email_address(text: str) -> bool:
    """
    Checks whether input text contains email address

    :param text: Input text
    :return: boolean
    """
    return bool(EMAIL_REGEX.findall(text))


