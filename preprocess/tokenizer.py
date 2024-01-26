import os
from file import *


from hazm import WordTokenizer
from file import *

punctuations = read_file("../data/punctuations.txt").split('\n')

word_tokenizer = WordTokenizer(join_verb_parts=True, replace_emails=True,
                               replace_ids=True, replace_links=True)


def tokenize(data):
    if os.path.exists("../data/raw_tokens.json"):
        print("tokenized already!")
        return open_json("../data/raw_tokens.json")

    print("tokenizing...")
    raw_tokens = []
    for string in data:
        raw_tokens.append(word_tokenizer.tokenize(string))
    write_json("../data/raw_tokens.json", raw_tokens)

    tokens_copy = raw_tokens.copy()
    for doc_id in range(tokens_copy.__len__()):
        for posting in range(tokens_copy[doc_id].__len__()):
            tokens_copy[doc_id][posting] = (tokens_copy[doc_id][posting], doc_id, posting)

    tokens = []
    for doc_token in tokens_copy:
        tokens.extend(doc_token)

    tokens = sort_tokens(tokens)
    tokens = remove_punc(tokens)
    write_json("../data/tokens.json", tokens)
    for i in range(100):
        print(tokens[i])

    print("tokenization done!")
    return raw_tokens


def sort_tokens(tokens):
    tokens = sorted(tokens, key=persian_sort_key)
    return tokens


def persian_sort_key(t):
    return [ord(c) for c in list(t[0])]


def remove_punc(tokens):
    result = []
    for token in tokens:
        flag = 0
        for punc in punctuations:
            if punc in token[0]:
                flag = 1
                break

        if flag == 1:
            continue

        result.append(token)

    return result
