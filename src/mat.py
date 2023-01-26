import numpy as np

a = set(np.load("data/ardelean_words.npy", allow_pickle=True).tolist())
b = set(np.load("data/banatean_words.npy", allow_pickle=True).tolist())
c = set(np.load("data/maramuresean_words.npy", allow_pickle=True).tolist())
d = set(np.load("data/moldovean_words.npy", allow_pickle=True).tolist())
e = set(np.load("data/oltean_words.npy", allow_pickle=True).tolist())


def iou(x, y):
    return len(x.intersection(y)) / len(x.union(y))

import spacy
v = [a, b, c, d, e]

min_num_values = min([len(x) for x in v])


def keep_only_n(my_set, num_values):
    my_new_set = set()
    for val in my_set:
        my_new_set.add(val)
        if len(my_new_set) >= num_values:
            return my_new_set

# v = [keep_only_n(sub_v, min_num_values) for sub_v in v]

nlp = spacy.load("ro_core_news_sm")

from tqdm import tqdm

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


v = convert_all_words_to_lemma(v)


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
