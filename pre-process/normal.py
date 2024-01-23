import file
import json
from hazm import Normalizer

normalized = False


def normalize_text(text):
    contents = " "
    for i in text:
        contents += text[i]['content']  # read just contents of files

    normalizer = Normalizer()
    contents = normalizer.normalize(contents)
    file.write_file("../data/normalized_text.txt", contents)
    # if normalization is done, normalized = True
    set_flag(True)
    return contents


def set_flag(state):
    global normalized
    normalized = state
