from tqdm import tqdm

import numpy as np

a = set(np.load("data/ardelean_words.npy", allow_pickle=True).tolist())
b = set(np.load("data/banatean_words.npy", allow_pickle=True).tolist())
c = set(np.load("data/maramuresean_words.npy", allow_pickle=True).tolist())
d = set(np.load("data/moldovean_words.npy", allow_pickle=True).tolist())
e = set(np.load("data/oltean_words.npy", allow_pickle=True).tolist())


unknown_dialects_books = ['data/books/Radu-Rosetti_Parintele-Zosim.pdf',
                          'data/books/povestipopulareromanesti1.pdf',
                          'data/books/101-Basme-Romanesti.pdf',
                          'data/books/Comorile poporului_Radulescu Constantin_Bucuresti_1930.pdf',
                          'data/books/Pop_Mihai_Obiceiuri_traditionale_romanesti_1999.pdf']

def iou(x, y, n = 5, only_word_n_characters_long: bool =True):
    if only_word_n_characters_long:
        to_remove = set()
        for elem in x:
            if len(elem) < n:
                to_remove.add(elem)
        x = x.difference(to_remove)
        to_remove = set()
        for elem in y:
            if len(elem) < n:
                to_remove.add(elem)
        y = y.difference(to_remove)
    return len(x.intersection(y)) / len(x.union(y))

from src.load_data import load_data
from nltk.tokenize import word_tokenize

v = [a, b, c, d, e]
dialects = ["ardelean", "banatean", "maramuresean", "moldovean", "oltean"]

# either entire books are in a dialect, either pages are in a dialect
# e.g. the whole book is ardelean, or pages 1, 3, 5, 8 are ardelean, pages 2,4,6,9 moldovean and pages 7, 10 oltean

for book_path in tqdm(unknown_dialects_books):
    print(book_path)
    whole_book_text = load_data(book_path, to_str=True)
    tokens = set(word_tokenize(whole_book_text))
    highest_iou = 0.0
    dialect_name = ""
    ious = []
    for (vec, dialect) in zip(v, dialects):
        det_iou = iou(tokens, vec)
        ious.append(det_iou)
        if det_iou > highest_iou:
            highest_iou = det_iou
            dialect_name = dialect
    print(book_path, dialect_name, highest_iou, ious)
    print("*" * 50)


import spacy

min_num_values = min([len(x) for x in v])

# sort = "ascending_by_word_length"

def keep_only_n(my_set, num_values):
    my_new_set = set()
    for val in my_set:
        my_new_set.add(val)
        if len(my_new_set) >= num_values:
            return my_new_set

# v = [keep_only_n(sub_v, min_num_values) for sub_v in v]

nlp = spacy.load("ro_core_news_sm")

def convert_all_words_to_lemma(v):
    for i in range(len(v)):
        b = set()
        for word in tqdm(v[i]):
            doc = nlp(word)
            for tok in doc:
                lemma_form = tok.lemma_
            b.add(lemma_form)
        v[i] = b
    return v


# v = convert_all_words_to_lemma(v)

mat = [[0 for _ in range(len(v))] for _ in range(len(v))]

for i in range(len(v)):
    for j in range(len(v)):
        print(i, j)
        mat[i][j] = round(iou(v[i], v[j]), 4)

# print(mat)
for i in range(len(v)):
    for j in range(len(v)):
        print(mat[i][j], end=" ")
    print()
