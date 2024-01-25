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
    result = [(item, count) for item, count in tokens if item not in punctuations]

    write_json("../data/no_punc_tokens.json", result)
    print("removed punctuations!")
    return result


# removes duplicates and adds a count element for each token
def remove_duplicates(tokens):
    if os.path.exists("../data/tokens_with_count.json"):
        print("duplicates removed!")
        return open_json("../data/tokens_with_count.json")

    print("removing duplicates...")
    result = Counter(tokens).most_common()
    write_json("../data/tokens_with_count.json", result)
    print("removed duplicates!")
    return result


def remove_stopwords(tokens):
    print("removing stopwords...")
    tokens_num = 0
    for (item, count) in tokens:
        tokens_num += count

    result = []
    stopwords = []
    for (item, count) in tokens:
        if (count / tokens_num * 100) > 0.1:
            stopwords.append((item, count))
            continue

        result.append((item, count))

    # stop_count = 0
    # for (word, count) in stopwords:
    #     print("({}: {})".format(word, count))
    #     stop_count += count

    # print("Total number of stopwords: {}".format(stop_count))
    print("removed stopwords!")
    return result


def lemma_tokens(tokens):
    if os.path.exists("../data/lemmatized_tokens.json"):
        print("lemmatized!")
        return open_json("../data/lemmatized_tokens.json")

    print("lemmatizing tokens...")
    text = []
    for token in tokens:
        text.extend(token)
    lemmatized = [lemmatizer.lemmatize(token) for token in text]
    write_json("../data/lemmatized_tokens.json", lemmatized)
    print("lemmatized tokens!")
    return lemmatized
