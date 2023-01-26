"""
translation inference
"""
from src.utils import dialectical_rules, dialect_to_formal_dict
import random

def text_to_speech(text):
    speech = text
    return speech

import pdb
import random
from src.tense_changer import *


def translate_from_dialect_to_formal(text, initial_dialect, modality: str="text"):
    """

    :param text:
    :param initial_dialect:
    :return:
    """
    fonetical_rules = dialectical_rules[initial_dialect]["fonetical_rules"]
    gramatical_rules = dialectical_rules[initial_dialect]["gramatical_rules"]

    # 1
    if initial_dialect in dialect_to_formal_dict.keys():
        final_dialect_words = dialect_to_formal_dict[initial_dialect]
        for (dialect_word, formal_word) in final_dialect_words.items():
            if dialect_word == dialect_word and formal_word == formal_word:
                gramatical_rules[dialect_word] = formal_word

    # 2
    if "fonetical_examples" in dialectical_rules[initial_dialect]:
        fonetical_examples = dialectical_rules[initial_dialect]["fonetical_examples"]
        for (k, v) in fonetical_examples.items():
            if v == v and k == k:
                fonetical_rules[k] = v

    # 3
    if "lexical_examples" in dialectical_rules[initial_dialect]:
        lexical_examples = dialectical_rules[initial_dialect]["lexical_examples"]
        for (k, v) in lexical_examples.items():
            if v == v and k == k:
                gramatical_rules[k] = v

    # 4
    if "gramatical_examples" in dialectical_rules[initial_dialect]:
        gramatical_examples = dialectical_rules[initial_dialect]["gramatical_examples"]
        for (k, v) in gramatical_examples.items():
            if v == v and k == k:
                gramatical_rules[k] = v

    to_remove_keys = []
    for (k, v) in fonetical_rules.items():
        if isinstance(k, str) is False or isinstance(v, str) is False:
            if isinstance(v, list):
                fonetical_rules[k] = random.choice(v)
            elif k != k or v != v:
                to_remove_keys.append(k)
            else:
                pdb.set_trace()

    for key in to_remove_keys:
        del fonetical_rules[key]

    fonetical_rules = sorted([(k, v) for (k, v) in fonetical_rules.items()], key=lambda x: (-1) * len(x[0]))

    to_remove_keys = []
    for (k, v) in gramatical_rules.items():
        if isinstance(k, str) is False or isinstance(v, str) is False:
            if isinstance(v, list):
                gramatical_rules[k] = random.choice(v)
            elif k != k or v != v:
                to_remove_keys.append(k)
            else:
                pdb.set_trace()

    for key in to_remove_keys:
        del gramatical_rules[key]

    gramatical_rules = sorted([(k, v) for (k, v) in gramatical_rules.items()], key=lambda x: (-1) * len(x[0]))

    if modality == "text":
        rules = gramatical_rules
    elif modality == "speech":
        rules = fonetical_rules
    else:
        raise Exception("Wrong!")

    if initial_dialect == "oltean":
        text = passe_simple_to_passe_compose(text)

    # 5 dialect to literal
    for (dialectical_form, literal_form) in rules:
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
    :param modality:
    :return:
    """
    fonetical_rules = dialectical_rules[final_dialect]["fonetical_rules"]
    gramatical_rules = dialectical_rules[final_dialect]["gramatical_rules"]

    # 1
    if final_dialect in dialect_to_formal_dict.keys():
        final_dialect_words = dialect_to_formal_dict[final_dialect]
        for (dialect_word, formal_word) in final_dialect_words.items():
            if formal_word == formal_word and dialect_word == dialect_word:
                gramatical_rules[dialect_word] = formal_word

    # 2
    if "fonetical_examples" in dialectical_rules[final_dialect]:
        fonetical_examples = dialectical_rules[final_dialect]["fonetical_examples"]
        for (k, v) in fonetical_examples.items():
            if v == v and k == k:
                fonetical_rules[k] = v

    # 3
    if "lexical_examples" in dialectical_rules[final_dialect]:
        lexical_examples = dialectical_rules[final_dialect]["lexical_examples"]
        for (k, v) in lexical_examples.items():
            if v == v and k == k:
                gramatical_rules[k] = v

    # 4
    if "gramatical_examples" in dialectical_rules[final_dialect]:
        gramatical_examples = dialectical_rules[final_dialect]["gramatical_examples"]
        for (k, v) in gramatical_examples.items():
            if v == v and k == k:
                gramatical_rules[k] = v

    to_remove_keys = []
    for (k, v) in fonetical_rules.items():
        if isinstance(k, str) is False or isinstance(v, str) is False:
            if isinstance(v, list):
                fonetical_rules[k] = random.choice(v)
            elif k != k or v != v:
                to_remove_keys.append(k)
            else:
                pdb.set_trace()

    for key in to_remove_keys:
        del fonetical_rules[key]

    fonetical_rules = sorted([(k, v) for (k, v) in fonetical_rules.items()], key=lambda x: (-1) * len(x[1]))

    to_remove_keys = []
    for (k, v) in gramatical_rules.items():
        if isinstance(k, str) is False or isinstance(v, str) is False:
            if isinstance(v, list):
                gramatical_rules[k] = random.choice(v)
            elif k != k or v != v:
                to_remove_keys.append(k)
            else:
                pdb.set_trace()

    for key in to_remove_keys:
        del gramatical_rules[key]

    gramatical_rules = sorted([(k, v) for (k, v) in gramatical_rules.items()], key=lambda x: (-1) * len(x[1]))

    if modality == "text":
        rules = gramatical_rules
    elif modality == "speech":
        rules = fonetical_rules
    else:
        raise Exception("Wrong!")

    if final_dialect == "oltean":
        text = passe_simple_to_passe_compose(text)

    # 5 literal to dialect
    for (dialectical_form, literal_form) in rules:
        if isinstance(dialectical_form, list):
            dialectical_form = random.choice(dialectical_form)
        text = text.replace(literal_form, dialectical_form)

    if modality == "speech":
        speech = text_to_speech(text)
        return speech

    return text


def translate(text: str, initial_dialect: str, final_dialect: str, modality: str="text"):
    """

    :param text:
    :param initial_dialect:
    :param final_dialect:
    :param modality:
    :return:
    """
    if initial_dialect == final_dialect:
        return "You need to translate between different dialects!"

    if initial_dialect != "formal":
        formal_text = translate_from_dialect_to_formal(text, initial_dialect, modality=modality)
    else:
        formal_text = text

    if final_dialect != "formal":
        final_translated_text = translate_from_formal_to_dialect(formal_text, final_dialect, modality=modality)
    else:
        final_translated_text = formal_text

    if modality == "speech":
        speech = text_to_speech(final_translated_text)
        return speech

    return final_translated_text


def main():
    text = "Ana are două picioare"
    print(translate(text, "formal", "moldovean", modality="text"))

    text = "Ion este pilot"
    print(translate(text, "formal", "moldovean", modality="text"))

    text = "No apăi unde merem amu?"
    print(translate(text, "ardelean", "formal", modality="text"))

    text = "Mă dusei să trec la Olt"
    print(translate(text, "formal", "oltean", modality="text"))

    text = "Și fași uăi?"
    print(translate(text, "moldovean", "formal", modality="text"))

    text = "Nu am decât zece lei la mine. Mă duc pă oraș mai pă seară, dupe mă duc acasă."
    print(translate(text, "formal", "ardelean", modality="text"))


if __name__ == "__main__":
    main()
