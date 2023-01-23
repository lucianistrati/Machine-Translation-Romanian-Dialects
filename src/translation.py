"""
translation inference
"""
def translate_from_dialect_to_formal(text, initial_dialect):
    """

    :param text:
    :param initial_dialect:
    :return:
    """
    pass


def translate_from_formal_to_dialect(text, final_dialect):
    """

    :param text:
    :param final_dialect:
    :return:
    """
    pass


def translate(text: str, initial_dialect: str, final_dialect: str):
    """

    :param text:
    :param initial_dialect:
    :param final_dialect:
    :return:
    """
    formal_text = translate_from_dialect_to_formal(text, initial_dialect)
    final_translated_text = translate_from_formal_to_dialect(text, final_dialect)
    return final_translated_text

def main():
    pass


if __name__ == "__main__":
    main()
