from document import *


# ye token ya term ya kalame tarif mikone, tedad kalame too kole doc-H ro migire save mikone
# ye list as doc-hayee ke kalame ro daran dare
class Token:
    def __init__(self, token, tf, docs):
        self.token = str(token)
        self.tf = tf
        self.docs = docs

    def add_doc(self, doc):
        self.docs.append(doc)

    def set_tf(self, tf):
        self.tf = tf

    def get_tf(self):
        return self.tf

    def get_token(self):
        return self.token

    def get_weight_in_doc(self, doc_index):
        return self.docs[doc_index].get_weight()
