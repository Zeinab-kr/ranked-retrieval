import bisect

from preprocess import file
from token_class import Token
import os


def make_index():
    tokens = []
    print("reading files...")
    if os.path.exists("../data/inverted_index.json"):
        tokens = file.open_json("../data/inverted_index.json")
        print(len(tokens))
        return tokens

    words = file.open_json("../data/tokens_with_count.json")  # (word, term_frequency)
    data = file.open_json("../data/tokens.json")  # (word, doc_id, posting)
    print("making indexes...")

    serializable = []
    counter = 0
    tokens.extend([Token])  # extend array by one
    tokens[0] = Token(words[0][0], words[0][1])  # set word and tf
    index = tokens[0].add_doc(data[0][1])  # data[0][1] -> doc_id
    tokens[0].set_weight(index, 1)
    tokens[0].add_posting_to_doc(index, data[0][2])
    print(len(data))
    print(len(words))

    # data: (word, doc_id, posting)   words: (word, tf)
    for i in range(1, len(data)):
        if counter == (len(words) - 1):
            break

        word = data[i][0]
        doc_id = data[i][1]
        posting = data[i][2]
        if word == data[i - 1][0]:  # if words are the same
            if doc_id == data[i - 1][1]:  # if focs are the same
                tokens[counter].increment_weight(index)
            else:  # if docs aren't the same
                index = tokens[counter].add_doc(doc_id)
                tokens[counter].set_weight(index, 1)
                tokens[counter].increment_df()

            tokens[counter].add_posting_to_doc(index, posting)
        else:  # if words aren't the same
            serializable.append({"token": tokens[counter].token,
                                 "tf": tokens[counter].tf,
                                 "df": tokens[counter].df,
                                "docs": tokens[counter].get_serializable_docs()})

            if counter % 1000 == 0:
                print("indexing part {}".format(int(counter / 1000)))
            counter += 1
            tokens.extend([Token])  # extend array by one
            tokens[counter] = Token(words[counter][0], words[counter][1])  # set word and tf
            index = tokens[counter].add_doc(doc_id)
            tokens[counter].set_weight(index, 1)
            tokens[counter].add_posting_to_doc(index, posting)

    serializable.append({"token": tokens[counter-1].token,
                         "tf": tokens[counter-1].tf,
                         "df": tokens[counter-1].df,
                        "postings_list": tokens[counter-1].get_serializable_docs()})
    file.write_json("../data/inverted_index.json", serializable)
    print("made indexes!")
    return tokens
