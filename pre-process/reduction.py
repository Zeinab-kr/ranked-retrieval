from collections import Counter
from hazm import WordTokenizer
import file


def find_stop_words(tokens):
    token_num = 0
    print("most common...")
    occurrence = Counter(tokens).most_common(50)
    print("most common done!")
    for token in occurrence:
        print(token)


def delete_punctuations(tokens):
    text = file.read_file("../data/punctuations.txt")
    punctuations = WordTokenizer().tokenize(text)
    print("deleting punctuations...")
    for punc in punctuations:
        if punc in tokens:
            for token in tokens:
                tokens.remove(punc)

    print("punctuations removed!")


