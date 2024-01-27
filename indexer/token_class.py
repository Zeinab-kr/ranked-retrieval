from document_class import *
from preprocess import file

doc_count = int(file.read_file("../data/number_of_docs.txt"))


class Token:
    def __init__(self, token, tf):
        self.token = str(token)
        self.tf = tf
        self.docs = []
        self.df = 1
        self.champion = []

    def add_doc(self, doc):
        self.docs.append(Document(doc))
        return len(self.docs) - 1

    def add_posting_to_doc(self, index, posting):
        self.docs[index].add_posting(posting)

    def set_weight(self, index, weight):
        self.docs[index].set_weight(weight)

    def increment_weight(self, index):
        self.docs[index].increment_weight()

    def increment_df(self):
        self.df = self.df + 1

    def set_df(self, df):
        self.df = df

    def set_tf(self, tf):
        self.tf = tf

    def get_tf(self):
        return self.tf

    def get_token(self):
        return self.token

    def get_weight_in_doc(self, doc_index):
        return self.docs[doc_index].get_weight()

    def get_docs(self):
        return self.docs

    def get_serializable_docs(self):
        result = []
        for doc in self.docs:
            result.append(doc.get_serializable_doc())

        return result
