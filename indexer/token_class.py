from document_class import *
from preprocess import file

doc_count = int(file.read_file("../data/number_of_docs.txt"))


# ye token ya term ya kalame tarif mikone, tedad kalame too kole doc-H ro migire save mikone
# ye list as doc-hayee ke kalame ro daran dare
class Token:
    def __init__(self, token, tf):
        self.token = str(token)
        self.tf = tf
        self.docs = []
        self.docs.extend([Document] * doc_count)

    def add_doc(self, doc):
        self.docs[doc] = Document(doc)

    def add_posting_to_doc(self, doc_id, posting):
        self.docs[doc_id].add_posting(posting)

    def set_weight(self, doc_id, weight):
        self.docs[doc_id].set_weight(weight)

    def increment_weight(self, doc_id):
        self.docs[doc_id].increment_weight()

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
