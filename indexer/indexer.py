import heapq
import time
import sys

from preprocess import file
from token_class import Token


def make_index():
    tokens = []
    print("reading files...")
    words = file.open_json("../data/tokens_with_count.json")  # (word, term_frequency)
    data = file.open_json("../data/tokens.json")  # (word, doc_id, posting)
    print("making indexes...")

    start_time = time.time()

    serializable = []
    counter = 0
    tokens.extend([Token])  # extend array by one
    word = words[0][0]
    tf = words[0][1]
    doc_id = data[0][1]
    posting = data[0][2]
    tokens[0] = Token(word, tf)  # set word and tf
    index = tokens[0].add_doc(doc_id)  # data[0][1] -> doc_id , returns index of added doc
    tokens[0].set_weight(index, 1)  # set weight of word in doc to 1
    tokens[0].add_posting_to_doc(index, posting)  # add posting

    # data: (word, doc_id, posting)   words: (word, tf)
    for i in range(1, len(data)):
        if counter == (len(words) - 1):
            break

        word, doc_id, posting = data[i]
        if word == data[i - 1][0]:  # if words are the same
            if doc_id == data[i - 1][1]:  # if docs are the same
                tokens[counter].increment_weight(index)  # increment weight in doc
            else:  # if docs aren't the same
                index = tokens[counter].add_doc(doc_id)  # add the new doc
                tokens[counter].set_weight(index, 1)  # set weight in doc to 1
                tokens[counter].increment_df()  # increment document frequency

            tokens[counter].add_posting_to_doc(index, posting)
        else:  # if words aren't the same
            # save data of the previous word in json serializable format
            weights = [(doc.doc_id, doc.weight) for doc in tokens[counter].docs]
            champion = heapq.nlargest(20, weights, key=lambda x: x[1])
            serializable.append({"token": tokens[counter].token,
                                 "tf": tokens[counter].tf,
                                 "df": tokens[counter].df,
                                 "champion": champion,
                                "docs": tokens[counter].get_serializable_docs()})

            if counter % 1000 == 0:
                print("indexing part {}".format(int(counter / 1000)))
            counter += 1
            tokens.extend([Token])  # extend array by one
            tokens[counter] = Token(words[counter][0], words[counter][1])  # set word and tf
            index = tokens[counter].add_doc(doc_id)
            tokens[counter].set_weight(index, 1)
            tokens[counter].add_posting_to_doc(index, posting)

    weights = [(doc.doc_id, doc.weight) for doc in tokens[counter-1].docs]
    champion = heapq.nlargest(20, weights, key=lambda x: x[1])
    serializable.append({"token": tokens[counter-1].token,
                         "tf": tokens[counter-1].tf,
                         "df": tokens[counter-1].df,
                         "champion": champion,
                        "postings_list": tokens[counter-1].get_serializable_docs()})

    temp = sorted(tokens, key=lambda x: len(x.docs))
    for i in range(len(temp) - 4, len(temp) - 1):
        print("word: {}, df: {}".format(temp[i].token, temp[i].df))
    print("made indexes!")
    end_time = time.time()
    print("time: {}".format(int(end_time - start_time)))
    print("saving data...")
    file.write_json("../data/inverted_index.json", serializable)
