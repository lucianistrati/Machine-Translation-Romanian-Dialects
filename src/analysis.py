"""
data analysis and visualization
"""
import os
from src.utils import class_to_book


def visualize():
    with open("data/all_books_contents.txt", "r") as f:
        books_contents = f.read()

    for book, file in zip(sorted(os.listdir("data/books")), books_contents):
        filepath = os.path.join("data/books", file)

        books_contents.append(texts)

    print(len(books_contents))




def main():
    pass


if __name__ == "__main__":
    main()
