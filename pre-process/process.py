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
    tokens = reduction.remove_duplicates(tokens)
    tokens = reduction.remove_punctuations(tokens)
    tokens = reduction.remove_numbers(tokens)


    for i in range(100):
        print(tokens[i])

    # if os.path.exists("../data/no_punc_tokens.json"):
    #     print("punctuations removed already")
    # else:
    #     reduction.delete_punctuations(tokens)
    #     file.write_json("../data/no_punc_tokens.json", tokens)
    #
    # os.system('cls')
    # reduction.find_stop_words(tokens)
