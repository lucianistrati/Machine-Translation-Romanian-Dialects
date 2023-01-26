import argparse
import spacy
from spacy.lang.ro.examples import sentences
import json
import pandas as pd
from spacy.matcher import Matcher

nlp = spacy.load("ro_core_news_lg")

conjugation = pd.read_json('conjugation-ro.json')
verbs = pd.read_json('verbs-ro.json')


def _get_matches(text):
    pattern = [[{'POS': 'AUX', "LEMMA": "avea"}, {'POS': 'VERB'}]]
    matcher = Matcher(nlp.vocab)
    matcher.add("verb-phrases", pattern)
    doc = nlp(text)
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


def main(text: str):
    matches = _get_matches(text)
    return sentence


if __name__ == "__main__":
    args = _build_parser()
    main(args.sentence)
