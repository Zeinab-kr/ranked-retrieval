from collections import Counter
from hazm import WordTokenizer
import file


def find_stop_words(tokens):
    token_num = 0
    occurrence = Counter(tokens).most_common(50)
    for token in occurrence:
        print(token)


def delete_punctuations(tokens):
    text = file.read_file("../data/punctuations.txt")
    punctuations = WordTokenizer().tokenize(text)
    for token in tokens:
        if token in punctuations:
            tokens.remove(token)
