import os

from hazm import WordTokenizer
from file import *

word_tokenizer = WordTokenizer(join_verb_parts=True, replace_emails=True,
                               replace_ids=True, replace_links=True)


def tokenize(data):
    if os.path.exists("../data/tokens.json"):
        print("tokenized already!")
        return open_json("../data/tokens.json")

    print("tokenizing...")
    tokens = []
    for string in data:
        tokens.append(word_tokenizer.tokenize(string))
    write_json("../data/tokens.json", tokens)
    print("tokenization done!")
    return tokens
