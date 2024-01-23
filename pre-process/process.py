import file
import normal
from hazm import WordTokenizer
import os
import tokenize
import reduction

reduced = False


def preprocess():
    data = file.open_json("../data/IR_data_news_12k.json")
    if not normal.normalized:
        normalized_data = normal.normalize_text(data)


    # tokens = WordTokenizer().tokenize(normalized_data)
    # reduction.delete_punctuations(tokens)
    # reduction.find_stop_words(tokens)
