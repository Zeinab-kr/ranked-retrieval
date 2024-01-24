import os

from hazm import WordTokenizer
import file


def tokenize(text):
    if os.path.exists("../data/tokens.json"):
        print("tokenized already!")
        return file.open_json("../data/tokens.json")

    print("tokenizing...")
    tokens = WordTokenizer(join_verb_parts=True, replace_emails=True,
                           replace_ids=True, replace_links=True).tokenize(text)
    file.write_json("../data/tokens.json", tokens)
    print("tokenization done!")
    return tokens