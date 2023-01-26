import argparse
import spacy
from spacy.lang.ro.examples import sentences
import os
from pathlib import Path
import pandas as pd
from spacy.matcher import Matcher

nlp = spacy.load("ro_core_news_lg")
folder = Path(__file__).parent
conjugation = pd.read_json(os.path.join(folder, 'conjugation-ro.json'))
verbs = pd.read_json(os.path.join(folder, 'verbs-ro.json'))


def _get_matches(doc):
    # pattern = [[{'POS': 'AUX', "LEMMA": "avea"}, {'POS': 'VERB'}]]
    pattern = [[{'POS': 'AUX'}, {'POS': 'VERB'}]]
    matcher = Matcher(nlp.vocab)
    matcher.add("verb-phrases", pattern)
    matches = matcher(doc)

    return matches


def _build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--sentence",
        help=f"sentence to change",
        type=str,
    )
    args = parser.parse_args()
    return args


def _get_person(doc, item):
    if doc[item[1] - 1].pos_ == "PRON":
        pron = doc[item[1] - 1]
    else:
        pron = doc[item[1]]
    persoana = int(pron.morph.get("Person")[0])
    if pron.morph.get("Number")[0] == "Plur":
        persoana += 3

    return persoana


def _get_result(persoana, template, root):
    result = root + conjugation[template]["Perfect"]['Perfect simplu'][persoana - 1][1]

    return result


def _change_tense(matches, doc, text):
    for item in matches:
        try:
            phrase = str(doc[item[1]:item[2]])
            participiu = doc[item[2] - 1].lemma_
            persoana = _get_person(doc, item)
            template = verbs[participiu]["template"]
            root = verbs[participiu]["root"]
            result = _get_result(persoana, template, root)

            text = text.replace(phrase, result, 1)
        except:
            pass
    return text


def main(text: str):
    doc = nlp(text)
    matches = _get_matches(doc)
    text = _change_tense(matches, doc, text)

    return text


if __name__ == "__main__":
    args = _build_parser()
    result = main(args.sentence)
    print(result)
