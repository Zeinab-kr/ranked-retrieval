import os

from file import *
import json
from hazm import Normalizer


def normalize_text(text):
    if os.path.exists("../data/normalized_text.txt"):
        print("normalized already!")
        return read_file("../data/normalized_text.txt")

    print("normalizing...")
    contents = " "
    for i in text:
        contents += " "
        contents += text[i]['content']  # read just contents of files

    normalizer = Normalizer()
    contents = normalizer.normalize(contents)
    addr = "../data/normalized_text.txt"
    write_file(addr, contents)
    print("normalization done!")
    return contents

