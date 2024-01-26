import bisect

from preprocess import file
import token_class
import document_class
import os

data = file.open_json("../data/tokens.json")
token = token_class.Token
document = document_class.Document


def make_index():
    tokens = []
    print("reading files...")
    if os.path.exists("../data/indexes.json"):
        tokens = file.open_json("../data/indexes.json")
        return tokens

    words = file.open_json("../data/final_tokens.json")
    print("making indexes...")
    words = sorted(words, key=persian_sort_key)
    print(data[0][1])

    counter = 0
    tokens.append(token(words[0][0], words[0][1]))
    tokens[0].extend_array(data[0][1])
    tokens[0].add_doc(data[0][1])
    tokens[0].set_weight(data[0][1], 1)
    tokens[0].add_posting_to_doc(data[0][1], data[0][2])

    # data: (word, doc_id, posting)   words: (word, tf)
    for i in range(1, len(data)):
        if data[i][0] == data[i-1][0]:  # if words are the same
            if data[i][1] == data[i-1][1]:  # if focs are the same
                tokens[i-1].increment_weight(data[i][1])
            else:  # if docs aren't the same
                tokens[i-1].extend_array(data[i][1])
                tokens[i-1].add_doc(data[i][1])
                tokens[i-1].set_weight(data[i][1], 1)

            tokens[i - 1].add_posting_to_doc(data[i][1], data[i][2])
        else:  # if words aren't the same
            counter += 1
            tokens.append(token(words[counter][0], words[counter][1]))  # add new index
            tokens[counter].extend_array(data[i][1])
            tokens[counter].add_doc(data[i][1])
            tokens[counter].set_weight(data[i][1], 1)
            tokens[counter].add_posting_to_doc(data[i][1], data[i][2])

        print("index {} made".format(counter))






    print("made indexes!")
    return tokens


def persian_sort_key(t):
    return [ord(c) for c in list(t[0])]
