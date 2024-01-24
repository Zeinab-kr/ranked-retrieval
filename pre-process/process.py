from file import open_json
from normal import *
from reduction import *
from tokenizer import *

reduced = False


def preprocess():
    print("opening file...")
    data = open_json("../data/IR_data_news_12k.json")
    print("file opened. Processing data...")

    normalized_data = normalize_text(data)
    tokens = tokenizer.tokenize(normalized_data)
    tokens = lemma_tokens(tokens)
    tokens = remove_duplicates(tokens)
    tokens = remove_punctuations(tokens)
    tokens = remove_stopwords(tokens)

    return tokens
