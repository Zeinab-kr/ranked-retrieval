import os

from file import *
import json
from hazm import Normalizer


def normalize_text(text):
    if os.path.exists("../data/normalized_text.json"):
        print("normalized already!")
        return open_json("../data/normalized_text.json")

    print("normalizing...")
    contents = []
    for i in text:
        temp = ""
        temp += str(text[i]['content'])  # read just contents of files
        contents.append(temp)

    normalizer = Normalizer()
    contents = [normalizer.normalize(content) for content in contents]
    addr = "../data/normalized_text.json"
    write_json(addr, contents)
    file = open("../data/normalized_text.txt", 'a', encoding='utf-8')
    for x in contents:
        file.write(x)
    print("normalization done!")
    return contents

