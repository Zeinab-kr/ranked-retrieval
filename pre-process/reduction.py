from collections import Counter
from hazm import WordTokenizer
import file


def find_stop_words(tokens):
    token_num = 0
    occurrence = Counter(tokens).most_common(50)
    for token in occurrence:
        print(token)

