import os.path
from collections import Counter
from hazm import WordTokenizer
from hazm import Stemmer
from hazm import Lemmatizer
from file import *

tokenizer = WordTokenizer()
lemmatizer = Lemmatizer()
stemmer = Stemmer()


def remove_punctuations(tokens):
    if os.path.exists("../data/no_punc_tokens.json"):
        print("punctuations removed!")
        return open_json("../data/no_punc_tokens.json")

    text = read_file("../data/punctuations.txt")
    punctuations = tokenizer.tokenize(text)
    print("deleting punctuations...")
    result = []
    flag = 0
    for token in tokens:
        if token[0] in punctuations:
            continue

        result.append(token)

    write_json("../data/no_punc_tokens.json", result)
    print("removed punctuations!")
    return result


# removes duplicates and adds a count element for each token
def remove_duplicates(tokens):
    if os.path.exists("../data/tokens_with_count.json"):
        print("duplicates removed!")
        return open_json("../data/tokens_with_count.json")

    print("removing duplicates...")
    data = []
    for word, i, j in tokens:
        data.append(word)

    result = Counter(data).most_common()
    write_json("../data/tokens_with_count.json", result)
    print("removed duplicates!")
    return result


def find_stopwords(tokens):
    print("removing stopwords...")
    tokens_num = 0
    for (item, count) in tokens:
        tokens_num += count

    stopwords = []
    for token in tokens:
        if (token[1] / tokens_num * 100) > 0.1:  # token[1] -> count of token
            stopwords.append(token)

    write_file("../data/number_of_tokens.txt", str(tokens_num))
    return stopwords


def remove_stopwords(stopwords, tokens):
    result = []
    for token in tokens:
        if token[0] in stopwords:
            continue

        result.append(token)

    print("removed stopwords!")

    return result


def lemma_tokens(tokens):
    if os.path.exists("../data/lemmatized_tokens.json"):
        print("lemmatized!")
        return open_json("../data/lemmatized_tokens.json")

    print("lemmatizing tokens...")
    lemmatized = []
    for word, i, j in tokens:
        lemmatized.append((lemmatizer.lemmatize(word), i, j))

    write_json("../data/lemmatized_tokens.json", lemmatized)
    print("lemmatized tokens!")
    return lemmatized
