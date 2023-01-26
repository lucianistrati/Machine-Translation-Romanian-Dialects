"""
data analysis and visualization
"""
import os
from src.utils import class_to_book, book_to_class
from src.load_data import load_data
import spacy

nlp = spacy.load("ro_core_news_sm")
# wordcloud

import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

some_other_stopwords = ["și", "la", "cu", "de", "mai", "pe", "se",
                        "în", "din", "care", "ce", "un", "să", "nu",
                        "lui", "o", "el", "după", "ea", "tot",
                        "numai", "ale", "nici", "să", "ca",
                        "o", "p", "t", "le", "te", "dă", "să",
                        "n", "fi", "s o", "s", "nu", "ne", "toate"]

"""
TODO remove moldovan_in_ukraine and replace with something else that is relevant
"""


def visualize():
    with open("data/all_books_contents.txt", "r") as f:
        books_contents = f.read()

    print(len(books_contents))
    from nltk.tokenize import word_tokenize
    for file in sorted(os.listdir("data/books")):
        if file not in book_to_class.keys():
            continue
        label = book_to_class[file]
        filepath = os.path.join("data/books", file)
        text = load_data(filepath, to_str=True)

        tokens = list(set(list(word_tokenize(text))))
        np.save(file=f"data/{label}_words.npy", allow_pickle=True, arr=np.array(tokens))

        doc = nlp(text[:int(1000000 * 0.25)])

        tokens = [token.text for token in doc if token.is_stop is False and
                  len(token.text) >= 2 and token.text[0] < "A" or token.text[0] > "Z"
                  and token.text not in some_other_stopwords]
        text = " ".join(tokens)
        print(file, len(text))
        # books_contents.append(texts)
        # Start with one review:
        # Create and generate a word cloud image:
        wordcloud = WordCloud(background_color="white").generate(text)

        # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        wordcloud.to_file(f"images/{label}.png")

    print(len(books_contents))


def main():
    visualize()


if __name__ == "__main__":
    main()
