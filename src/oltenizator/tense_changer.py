import argparse
import spacy
from spacy.lang.ro.examples import sentences
import os
from pathlib import Path
import pandas as pd
from spacy.matcher import Matcher

nlp = spacy.load("ro_core_news_sm")
folder = Path(__file__).parent
conjugation = pd.read_json(os.path.join(folder, 'conjugari.json'))
verbs = pd.read_json(os.path.join(folder, 'verbe.json'))


def _get_matches(doc, text_type=None):
    # pattern = [[{'POS': 'AUX', "LEMMA": "avea"}, {'POS': 'VERB'}]]
    pattern = [[{'POS': 'AUX'}, {'POS': 'VERB'}]]
    if text_type:
        pattern = [[{'POS': 'VERB'}]]
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
    parser.add_argument(
        "-r",
        "--reverse",
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

def _get_result_reverse(persoana, template, root):
    result = root + conjugation[template]["Perfect"]['Perfect compus'][persoana - 1][1]

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

def _change_tense_reverse(matches, doc, text):
    for item in matches:
        morph_features = doc[item[1]].morph
        if morph_features.get("Mood")[0] == "Ind" and morph_features.get("Tense")[0] == "Past" and morph_features.get("VerbForm")[0] == "Fin":
            try:
                phrase = str(doc[item[1]:item[2]])
                participiu = doc[item[1]].lemma_
                persoana = _get_person(doc, item)
                template = verbs[participiu]["template"]
                root = verbs[participiu]["root"]
                result = _get_result_reverse(persoana, template, root)
                lookup = ["am", "ai", "are", "avem", "aveţi", "au"]
                result = lookup[persoana-1] + " " + result
                text = text.replace(phrase, result, 1)
            except:
                pass
    return text


def passe_simple_to_passe_compose(text: str) -> str:
    doc = nlp(text)
    matches = _get_matches(doc, True)
    text = _change_tense_reverse(matches, doc, text)
    return text

def passe_compose_to_passe_simple(text: str) -> str:
    doc = nlp(text)
    matches = _get_matches(doc)
    text = _change_tense(matches, doc, text)
    return text

def main(text: str, text_type = None):
    doc = nlp(text)
    matches = _get_matches(doc, text_type)
    if text_type:
        text = _change_tense_reverse(matches, doc, text)
    else:
        text = _change_tense(matches, doc, text)


    return text


if __name__ == "__main__":
    args = _build_parser()
    result = main(args.sentence, args.reverse)
    print(result)
