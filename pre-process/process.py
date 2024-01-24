from collections import Counter
import file
import normal
import reduction
import tokenizer

reduced = False


def preprocess():
    print("opening file...")
    data = file.open_json("../data/IR_data_news_12k.json")
    print("file opened. Processing data...")

    normalized_data = normal.normalize_text(data)
    tokens = tokenizer.tokenize(normalized_data)

    freq_tokens = Counter(tokens).most_common()

    # if os.path.exists("../data/no_punc_tokens.json"):
    #     print("punctuations removed already")
    # else:
    #     reduction.delete_punctuations(tokens)
    #     file.write_json("../data/no_punc_tokens.json", tokens)
    #
    # os.system('cls')
    # reduction.find_stop_words(tokens)
