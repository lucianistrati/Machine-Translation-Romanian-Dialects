"""
two of the following models/systems should be trained here:
 - model for dialect detection
 - model for translating from standard Romanian to a dialect and viceversa
"""
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from src.load_data import load_data
from nltk.tokenize import sent_tokenize

import numpy as np

import os


def train_translation_model():
    # would be nice tho there is not really time for this
    pass

def main():
    book_to_class = {'dstef_antologie-de-folclor-din-maramures.pdf': 'maramuresean',
                     'Poezi-in-grai-banatean-vol1.pdf': 'banatean',
                     'Ion_Pop_Reteganul_Poveti_ardeleneti_Ba.pdf': 'ardelean',
                     'Dilibau. Povesti oltenesti - Cristiana Belodan.pdf': 'oltean',
                     'Moldovan_in_Ukraine_01.pdf': 'moldovean'}

    class_to_idx = {"maramuresean": 0,
                    "banatean": 1,
                    "ardelean": 2,
                    "oltean": 3,
                    "moldovean": 4
                    }

    targets_names = ["maramuresean", "banatean", "ardelean", "oltean", "moldovean"]
    X, y = [], []
    import nltk
    # nltk.download("punkt")
    # nltk.download('averaged_perceptron_tagger')
    # nltk.download('all')
    import spacy
    import random
    nlp = spacy.load("ro_core_news_sm")
    for (filename, label) in book_to_class.items():
        filepath = os.path.join("data/books/", filename)
        book_lines = load_data(filepath=filepath, to_str=False)
        idx = class_to_idx[label]
        for line in book_lines:
            doc = nlp(line)
            # sentences = sent_tokenize(text=line, language="en")
            sentences = []
            sentence = ""
            for token in doc:
                sentence += (token.text + " ")
                if len(sentence) > random.randint(100, 300):
                    sentences.append(sentence)
                    sentence = ""
            for sentence in sentences:
                X.append(sentence)
                y.append(idx)
            # for sentence in doc.sents:
                # X.append(sentence.text)
                # y.append(idx)

    # np.save(file="data/X.npy", allow_pickle=True, arr=np.array(X))
    # np.save(file="data/y.npy", allow_pickle=True, arr=np.array(y))

    np.save(file="data/X.npy", allow_pickle=True, arr=np.array(X))
    np.save(file="data/y.npy", allow_pickle=True, arr=np.array(y))

    from collections import Counter
    print("Number of sentences overall: ", len(X), len(y))
    print("Classes distribution: ", Counter(y))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

    from sklearn.svm import SVC
    from sklearn.metrics import f1_score, classification_report

    cv = CountVectorizer()
    X_train = cv.fit_transform(X_train)
    X_test = cv.transform(X_test)
    model = SVC()

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("F1 weighted:", f1_score(y_pred, y_test, average="weighted"))

    print(classification_report(y_pred, y_test, target_names=targets_names))


if __name__ == "__main__":
    main()
