import os

from normal import *
from reduction import *
from hazm import WordTokenizer
from file import *

word_tokenizer = WordTokenizer(join_verb_parts=True, replace_emails=True,
                               replace_ids=True, replace_links=True)


def preprocess():
    print("opening file...")
    data = open_json("../data/IR_data_news_12k.json")
    print("file opened. Processing data...")

    normalized_data = normalize_text(data)  # returns an array of strings

    if os.path.exists("../data/raw_tokens.json"):
        print("tokenized already!")
        tokenized = open_json("../data/raw_tokens.json")
    else:
        tokenized = []
        print("tokenizing...")
        for string in normalized_data:
            tokenized.append(word_tokenizer.tokenize(string))  # two-dimensional array of words

        write_json("../data/raw_tokens.json", tokenized)
        print("tokenization done!")

    tokens = []  # (word, posting)
    for i in range(len(tokenized)):
        for j in range(len(tokenized[i])):
            tokens.append((tokenized[i][j],  i, j))

    tokens = lemma_tokens(tokens)  # (lemmatized_token, doc_id, posting)
    tokens = remove_punctuations(tokens)
    count_tokens = remove_duplicates(tokens)  # returns (token, count)
    stopwords = find_stopwords(count_tokens)
    tokens = remove_stopwords(stopwords, tokens)  # returns (token, doc_id, posting)
    count_tokens = remove_duplicates(tokens)

    print("sorting...")
    tokens = sort_tokens(tokens)
    count_tokens = sort_tokens(count_tokens)
    print("sorting done!")
    write_json("../data/tokens.json", tokens)
    write_json("../data/tokens_with_count.json", count_tokens)
    write_file("../data/number_of_docs.txt", str(len(normalized_data)))


def sort_tokens(tokens):
    tokens = sorted(tokens, key=persian_sort_key)
    return tokens


def persian_sort_key(t):
    return [ord(c) for c in list(t[0])]
