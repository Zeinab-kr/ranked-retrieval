from file import *
from token import *
import os

data = open_json("../data/tokens.json")


def make_index():
    tokens = []
    if os.path.exists("../data/indexes.json"):
        tokens = open_json("../data/indexes.json")
        return tokens

    words = open_json("../data/final_tokens.json")
    for word, count in words:
        tokens.append(Token(word, count, find_in_file(word)))

    return tokens


def find_in_file(word):
    docs = []
    for doc in data:
        if word in doc:
            (w, positions) = find_positions(data.index(doc), word)
            docs.append(Document(w, positions))

    return docs


def find_positions(doc_index, word_to_search):
    positions = []
    w = 0  # weight of the word in doc
    for word in data[doc_index]:
        if word == word_to_search:
            positions.append(data[doc_index].index(word))
            w += 1

    return w, positions
