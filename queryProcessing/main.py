import indexer
#import process
#from queryProcessor import process_query


def main():
    #process.preprocess()
    indexer.make_index()
    #query = input("Enter your query: ")
    #results = process_query(query)
    #for doc_id, similarity, url in results:
    #    print("Similarity: {:.2F}\turl: {}".format(similarity, url))


if __name__ == "__main__":
    main()
