import file
import normal
import os

reduced = False


def preprocess():
    data = file.open_json("../data/IR_data_news_12k.json")
    if os.path.exists("../data/normalized_text.txt"):
        normalized_data = file.read_file("../data/normalized_text.txt")
    else:
        print("normalizing...")
        normalized_data = normal.normalize_text(data)
        print("normalization done!")

    if os.path.exists("../data/tokens.json"):
        tokens = file.open_json("../data/tokens.json")
    else:
        print("tokenizing...")
        tokens = normalized_data.split(" .،؛:)(/!؟@#%^&*$[]}{")
        file.write_json("../data/tokens.json", tokens)
        print("tokenization done!")


    # reduction.find_stop_words(tokens)
