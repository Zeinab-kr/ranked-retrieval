import math
from collections import Counter

from preprocess import file

# token, tf, df, champion_list, docs and postings
inverted_index = file.open_json("../data/inverted_index.json")
number_of_docs = int(file.read_file("../data/number_of_docs.txt"))


def doc_to_vector(word):
    word_index = binary_search(word)
    df = word_index["df"]
    idf = number_of_docs // df
    docs = word_index["docs"]  # {"doc_id", "weight", "positions"}
    result = []
    for doc in docs:
        tf = 1 + math.log10(doc["weight"])
        tf_idf = tf * idf
        result.append((word, doc["doc_id"], tf_idf))

    result = sorted(result)
    return result  # result -> (word, doc_id, tf_idf)


def query_to_vector(query):
    with_count = Counter(query).most_common()
    with_count = sorted(with_count)
    result = []
    for word, count in with_count:
        tf = 1 + math.log10(count)
        result.append((word, tf))

    return result  # (word, tf)


def binary_search(word):
    left = 0
    right = len(inverted_index) - 1
    while left <= right:
        mid = (left + right) // 2
        if inverted_index[mid]["token"] == word:
            return inverted_index[mid]  # Word found at index mid
        elif inverted_index[mid]["token"] < word:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half
    return -1  # Word not found
