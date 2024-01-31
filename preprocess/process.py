import os
import time

from normal import *
from reduction import *
from hazm import WordTokenizer
from file import *

word_tokenizer = WordTokenizer(join_verb_parts=True, replace_emails=True,
                               replace_ids=True, replace_links=True)


def preprocess():
    start_time = time.time()
    print("opening file...")
    data = open_json("../data/IR_data_news_5k 2.json")
    print("file opened. Processing data...")

    print()

    normalized_data = normalize_text(data)  # returns an array of strings

    # tokenizing
    print("tokenizing...")
    tokens = []  # (word, doc_id, posting)
    for i in normalized_data:
        tokenized_string = word_tokenizer.tokenize(normalized_data[i])
        for j, word in enumerate(tokenized_string):
            tokens.append((word, i, j))

    print("tokenized!")
    tokens = lemma_tokens(tokens)  # (lemmatized_token, doc_id, posting)
    tokens = remove_punctuations(tokens)
    count_tokens = remove_duplicates(tokens)  # returns (token, count)
    stopwords = find_stopwords(count_tokens, len(tokens))
    tokens = remove_stopwords(stopwords, tokens)  # returns (token, doc_id, posting)
    count_tokens = remove_duplicates(tokens)  # (token, count)

    print("sorting...")
    tokens = sorted(tokens, key=persian_sort_key)
    count_tokens = sorted(count_tokens, key=persian_sort_key)
    print("sorting done!")
    print("preprocessing done!")
    end_time = time.time()
    print("time: {}".format(int(end_time - start_time)))
    print("saving data...")
    write_json("../data/tokens.json", tokens)
    write_json("../data/tokens_with_count.json", count_tokens)
    write_file("../data/number_of_docs.txt", str(len(normalized_data)))


def persian_sort_key(t):
    return [ord(c) for c in list(t[0])]
