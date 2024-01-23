import file
import json
from hazm import Normalizer


def normalize_text(text):
    contents = " "
    for i in text:
        contents += " "
        contents += text[i]['content']  # read just contents of files

    normalizer = Normalizer()
    contents = normalizer.normalize(contents)
    addr = "../data/normalized_text.txt"
    file.write_file(addr, contents)
    return contents

