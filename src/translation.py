"""
translation inference
"""
from src.utils import dialectical_rules, dialect_to_formal_dict
import random

def text_to_speech(text):
    speech = None
    return speech


def translate_from_dialect_to_formal(text, initial_dialect, modality: str="text"):
    """

    :param text:
    :param initial_dialect:
    :return:
    """
    fonetical_rules = dialectical_rules[initial_dialect]["fonetical_rules"]
    gramatical_rules = dialectical_rules[initial_dialect]["gramatical_rules"]

    if initial_dialect in dialect_to_formal_dict.keys():
        final_dialect_words = dialect_to_formal_dict[initial_dialect]
        for (dialect_word, formal_word) in final_dialect_words.items():
            gramatical_rules[dialect_word] = formal_word

    if "fonetical_examples" in dialectical_rules[initial_dialect]:
        fonetical_examples = dialectical_rules[initial_dialect]["fonetical_examples"]
        for (k, v) in fonetical_examples.items():
            fonetical_rules[k] = v

    if "lexical_examples" in dialectical_rules[initial_dialect]:
        lexical_examples = dialectical_rules[initial_dialect]["lexical_examples"]
        for (k, v) in lexical_examples.items():
            gramatical_rules[k] = v

    if "gramatical_examples" in dialectical_rules[initial_dialect]:
        gramatical_examples = dialectical_rules[initial_dialect]["gramatical_examples"]
        for (k, v) in gramatical_examples.items():
            gramatical_rules[k] = v

    if modality == "text":
        rules = gramatical_rules
    elif modality == "speech":
        rules = fonetical_rules
    else:
        raise Exception("Wrong!")

    for (literal_form, dialectical_form) in rules.keys():
        if isinstance(dialectical_form, list):
            dialectical_form = random.choice(dialectical_form)
        text = text.replace(dialectical_form, literal_form)

    if modality == "speech":
        speech = text_to_speech(text)
        return speech

    return text

def translate_from_formal_to_dialect(text, final_dialect, modality: str="text"):
    """

    :param text:
    :param final_dialect:
    :return:
    """
    fonetical_rules = dialectical_rules[final_dialect]["fonetical_rules"]
    gramatical_rules = dialectical_rules[final_dialect]["gramatical_rules"]

    if final_dialect in dialect_to_formal_dict.keys():
        final_dialect_words = dialect_to_formal_dict[final_dialect]
        for (dialect_word, formal_word) in final_dialect_words.items():
            gramatical_rules[formal_word] = dialect_word

    if "fonetical_examples" in dialectical_rules[final_dialect]:
        fonetical_examples = dialectical_rules[final_dialect]["fonetical_examples"]
        for (k, v) in fonetical_examples.items():
            fonetical_rules[k] = v

    if "lexical_examples" in dialectical_rules[final_dialect]:
        lexical_examples = dialectical_rules[final_dialect]["lexical_examples"]
        for (k, v) in lexical_examples.items():
            gramatical_rules[k] = v

    if "gramatical_examples" in dialectical_rules[final_dialect]:
        gramatical_examples = dialectical_rules[final_dialect]["gramatical_examples"]
        for (k, v) in gramatical_examples.items():
            gramatical_rules[k] = v

    if modality == "text":
        rules = gramatical_rules
    elif modality == "speech":
        rules = fonetical_rules
    else:
        raise Exception("Wrong!")

    for (literal_form, dialectical_form) in rules.keys():
        if isinstance(dialectical_form, list):
            dialectical_form = random.choice(dialectical_form)
        text = text.replace(literal_form, dialectical_form)

    if modality == "speech":
        speech = text_to_speech(text)
        return speech

    return text


def translate(text: str, initial_dialect: str, final_dialect: str):
    """

    :param text:
    :param initial_dialect:
    :param final_dialect:
    :return:
    """
    if initial_dialect == final_dialect:
        return "You need to translate between different dialects!"

    if initial_dialect != "formal":
        formal_text = translate_from_dialect_to_formal(text, initial_dialect)
    else:
        formal_text = text

    if final_dialect != "formal":
        final_translated_text = translate_from_formal_to_dialect(formal_text, final_dialect)
    else:
        final_translated_text = formal_text

    return final_translated_text


def main():
    text = "Ana are mere"
    translate(text, "muntean", "moldovean")


if __name__ == "__main__":
    main()
