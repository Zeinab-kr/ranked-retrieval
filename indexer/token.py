from document import *


# ye token ya term ya kalame tarif mikone, tedad kalame too kole doc-H ro migire save mikone
# ye list as doc-hayee ke kalame ro daran dare
class Token:
    def __init__(self, tf):
        self.tf = tf
        self.docs = []

    def add_doc(self, weight):
        self.docs.append(Document(weight))

    def add_posting(self, doc_index, posting):
        self.docs[doc_index].add_posting(posting)

