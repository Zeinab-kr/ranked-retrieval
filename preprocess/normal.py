from hazm import Normalizer


def normalize_text(text):
    print("normalizing...")
    contents = {}
    normalizer = Normalizer()
    for i in text:
        temp = ""
        temp += str(text[i]['content'])  # read just contents of files
        contents[i] = normalizer.normalize(temp)

    print("normalized:\n{}".format(contents["4092"]))
    print("normalization done!")
    return contents

