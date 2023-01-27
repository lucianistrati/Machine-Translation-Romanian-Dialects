from typing import Dict, List, Set, Tuple, Optional, Any, Callable, NoReturn, Union, Mapping, Sequence, Iterable
from gensim.test.utils import common_texts
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec
from nltk.corpus import stopwords

import matplotlib.pyplot as plt

import multiprocessing
import nltk
import pdb


def document_preprocess(document):
    """
    :param document:
    :return:
    """
    return word_tokenize(document)

import os
import random
import spacy
from src.load_data import load_data
nlp = spacy.load("ro_core_news_sm")
from tqdm import tqdm

def main():
    texts = []
    for file in sorted(os.listdir("data/books")):
        filepath = os.path.join("data/books", file)
        lines = load_data(filepath, to_str=False)
        for line in tqdm(lines):
            doc = nlp(line)
            sentence = ""
            for token in doc:
                sentence += (token.text + " ")
                if len(sentence) > random.randint(50, 300):
                    texts.append(sentence)
                    sentence = ""

    texts_ = []
    for text in texts:
        try:
            processed_text = document_preprocess(text)
        except:
            continue
        texts_.append(processed_text)
    texts = texts_
    # texts = [document_preprocess(text) for text in texts]

    print(multiprocessing.cpu_count())

    print(texts[0])
    print(texts[-1])
    model = Word2Vec(sentences=texts, vector_size=300, window=5, min_count=1,
                     workers=multiprocessing.cpu_count())

    model.save("checkpoints/word2vec.model")  # checkpoint is saved

    print("saved")

from statistics import mean


def load_word2vec():
    model = Word2Vec.load("checkpoints/word2vec.model")
    return model

def predict_word2vec(text, model):
    preproc_text = document_preprocess(text)
    return mean([model.wv[word] for word in preproc_text])


if __name__ == "__main__":
    main()