from collections import Counter
from hazm import WordTokenizer
from hazm import Stemmer
from hazm import Lemmatizer
from file import *

tokenizer = WordTokenizer()
lemmatizer = Lemmatizer()
stemmer = Stemmer()


def remove_punctuations(tokens):
    text = read_file("../data/punctuations.txt")
    punctuations = tokenizer.tokenize(text)
    print("removing punctuations...")
    result = [token for token in tokens if token[0] not in punctuations]
    print("removed punctuations!")
    return result


# removes duplicates and adds a count element for each token
def remove_duplicates(tokens):
    data = [word for word, i, j in tokens]
    result = Counter(data).most_common()
    return result


def find_stopwords(tokens, tokens_num):
    print("removing stopwords...")
    stopwords = []
    for token in tokens:
        if (token[1] / tokens_num * 100) > 0.1:  # token[1] -> count of token
            stopwords.append(token[0])
        else:  # because the list is sorted by count
            break

    write_json("../data/stopwords.json", stopwords)
    write_file("../data/number_of_tokens.txt", str(tokens_num))
    return stopwords


def remove_stopwords(stopwords, tokens):
    result = [token for token in tokens if token[0] not in stopwords]
    print("removed stopwords!")

    return result


def lemma_tokens(tokens):
    print("lemmatizing tokens...")
    lemmatized = [(lemmatizer.lemmatize(word), i, j) for word, i, j in tokens]
    print("lemmatized tokens!")
    return lemmatized
