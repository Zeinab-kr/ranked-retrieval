import heapq

from preprocess import file
from hazm import WordTokenizer, Normalizer, Lemmatizer
from vectorizer import doc_to_vector, query_to_vector

normalizer = Normalizer()
lemmatizer = Lemmatizer()
tokenizer = WordTokenizer()

data = file.open_json("../data/IR_data_news_5k 2.json")
punctuations = tokenizer.tokenize(file.read_file("../data/punctuations.txt"))
stopwords = file.open_json("../data/stopwords.json")


def preprocess_query(query):
    # pre-processing the query
    print("preprocessing query...")
    query = normalizer.normalize(query)
    query = tokenizer.tokenize(query)
    query = [lemmatizer.lemmatize(word) for word in query]
    query = [item for item in query if item not in punctuations]
    query = [item for item in query if item not in stopwords]
    return query


def process_query(query):
    query = preprocess_query(query)
    doc_vectors = []
    for word in query:
        doc_vectors.extend(doc_to_vector(word))

    query_vector = query_to_vector(query)
    similarity = cosine_value(query_vector, doc_vectors)
    similar_docs = dict(heapq.nlargest(20, similarity.items(), key=lambda item: item[1]))
    doc_links = [(doc_id, similar_docs[doc_id], data[str(doc_id)]["content"]) for doc_id in similar_docs if
                 str(doc_id) in data]
    return doc_links


def cosine_value(query_vector, doc_vectors):
    docs = {}
    for word, doc_id, tf_idf in doc_vectors:  # dictionary representation of doc_vectors
        docs[doc_id] = {word: tf_idf}

    query_vector_size = 0
    for word, tf in query_vector:
        query_vector_size += (tf * tf)

    query_vector_size = query_vector_size ** 0.5

    dot_products = {}
    doc_vectors_size = {}
    for doc_id in docs:
        doc_vectors_size[doc_id] = 0
        dot_products[doc_id] = 0
        for word, tf in query_vector:
            if word in docs[doc_id]:
                product = docs[doc_id][word] * tf
                dot_products[doc_id] += product

        for word in docs[doc_id]:
            doc_vectors_size[doc_id] += (docs[doc_id][word] * docs[doc_id][word])

    for doc_id in doc_vectors_size:
        doc_vectors_size[doc_id] = doc_vectors_size[doc_id] ** 0.5

    similarity = {}
    for doc_id in dot_products:
        similarity[doc_id] = dot_products[doc_id] / (doc_vectors_size[doc_id] * query_vector_size)

    return similarity  # {doc_id: cosine_value}
