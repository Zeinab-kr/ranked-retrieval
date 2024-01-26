import bisect

from preprocess import file
from token_class import Token
import os

data = file.open_json("../data/tokens.json")


def make_index():
    tokens = []
    tokens.extend([Token])
    print("reading files...")
    if os.path.exists("../data/indexes.json"):
        tokens = file.open_json("../data/indexes.json")
        return tokens

    words = file.open_json("../data/final_tokens.json")
    print("making indexes...")
    words = sorted(words, key=persian_sort_key)
    print(data[0][1])

    counter = 0
    tokens[0] = Token(words[0][0], words[0][1])
    tokens[0].add_doc(data[0][1])
    tokens[0].set_weight(data[0][1], 1)
    tokens[0].add_posting_to_doc(data[0][1], data[0][2])

    # data: (word, doc_id, posting)   words: (word, tf)
    for i in range(1, len(data)):
        if i % 10000 == 0:
            print("making index part {}".format(i/10000))

        word = data[i][0]
        doc_id = data[i][1]
        posting = data[i][2]
        if word == data[i-1][0]:  # if words are the same
            if doc_id == data[i-1][1]:  # if focs are the same
                tokens[counter].increment_weight(doc_id)
            else:  # if docs aren't the same
                tokens[counter].add_doc(doc_id)
                tokens[counter].set_weight(doc_id, 1)

            tokens[counter].add_posting_to_doc(doc_id, posting)
        else:  # if words aren't the same
            counter += 1
            tokens.extend([Token])
            tokens[counter] = Token(words[counter][0], words[counter][1])  # add new index
            tokens[counter].add_doc(doc_id)
            tokens[counter].set_weight(doc_id, 1)
            tokens[counter].add_posting_to_doc(doc_id, posting)






    print("made indexes!")
    return tokens


def persian_sort_key(t):
    return [ord(c) for c in list(t[0])]
