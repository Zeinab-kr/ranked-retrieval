import os.path
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


def remove_punctuations(tokens):
    if os.path.exists("../data/no_punc_tokens.json"):
        print("punctuations removed already")
        return file.open_json("../data/no_punc_tokens.json")

    text = file.read_file("../data/punctuations.txt")
    punctuations = WordTokenizer().tokenize(text)
    print("deleting punctuations...")
    result = [(item, count) for item, count in tokens if item not in punctuations]

    file.write_json("../data/no_punc_tokens.json", tokens)
    print("punctuations removed!")
    return result


# removes duplicates and adds a count element for each token
def remove_duplicates(tokens):
    if os.path.exists("../data/tokens_with_count.json"):
        print("removed duplicates already")
        return file.open_json("../data/tokens_with_count.json")

    print("removing duplicates...")
    result = Counter(tokens).most_common()
    file.write_json("../data/tokens_with_count.json", result)
    return result


def remove_numbers(tokens):
    if os.path.exists("../data/no_num_punc_dup.json"):
        print("removed numbers already")
        return file.open_json("../data/no_num_punc_dup.json")

    print("removing numbers...")
    result = [(item, count) for item, count in tokens if not (item.isdigit() or item == 'NUM' or item == 'NUMF')]
    file.write_json('../data/no_num_punc_dup.json', result)
    print("numbers removed")
    return result
