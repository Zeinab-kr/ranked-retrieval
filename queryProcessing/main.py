from indexer import indexer
from preprocess import process
import time

from queryProcessor import process_query


def main():
    process.preprocess()
    indexer.make_index()
    query = input("Enter your query: ")
    start_time = time.time()
    results = process_query(query)
    for doc_id, similarity, url in results:
        print("Similarity: {}\turl: {}".format(similarity, url))

    # for doc_id, url in results:
    #     print("url: {}".format(url))

    end_time = time.time()
    print("time: {}".format(end_time - start_time))


if __name__ == "__main__":
    main()
