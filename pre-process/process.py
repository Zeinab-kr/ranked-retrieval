import file
import normal
from hazm import WordTokenizer
import os
import tokenize
import reduction

reduced = False


def preprocess():
    data = file.open_json("../data/IR_data_news_12k.json")
    if os.path.exists("../data/normalized_text.txt"):
        normalized_data = file.read_file("../data/normalized_text.txt")
    else:
        normalized_data = normal.normalize_text(data)

    if os.path.exists("../data/tokens.json"):
        tokens = file.open_json("../data/tokens.json")
    else:
        tokens = WordTokenizer().tokenize(normalized_data)
        file.write_json("../data/tokens.json", tokens)

    
    # reduction.delete_punctuations(tokens)
    # reduction.find_stop_words(tokens)
