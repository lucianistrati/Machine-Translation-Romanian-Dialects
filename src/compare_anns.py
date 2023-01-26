import os

from src.load_data import load_data

import enchant

def compare():
    method_of_comparison = "levenshtein"
    ann_filepath = "data/transcriptions/annotations/About our village and our language – Timok Romanian (Vlach) Collection.txt"

    pred_filepath = "data/transcriptions/vatis_tech/timok.txt"
    pred_2_filepath = "data/transcriptions/sonix/About our village and our language  Timok Romanian Vlach Collection.mp4.txt"

    ann = load_data(ann_filepath, to_str=True, strip=True, no_diacritics=True)
    pred_1 = load_data(pred_filepath, to_str=True, strip=True, no_diacritics=True)
    pred_2 = load_data(pred_2_filepath, to_str=True, strip=True, no_diacritics=True)

    print("Annotation length: ", len(ann))
    print("Prediction length: ", len(pred_1))
    print("Max string length: ", max(len(pred_1), len(ann)))
    print("Normalized levenshtein distance: ", enchant.utils.levenshtein(ann, pred_1) / max(len(pred_1), len(ann)))

    print("Annotation length: ", len(ann))
    print("Prediction length: ", len(pred_2))
    print("Max string length: ", max(len(pred_2), len(ann)))
    print("Normalized levenshtein distance: ", enchant.utils.levenshtein(ann, pred_2) / max(len(pred_2), len(ann)))


def main():
    compare()


if __name__ == "__main__":
    main()
