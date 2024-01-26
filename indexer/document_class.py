class Document:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.weight = 0
        self.positions = []

    def add_posting(self, pos):
        self.positions.append(pos)

    def set_weight(self, weight):
        self.weight = weight

    def increment_weight(self):
        self.weight = self.weight + 1

    def get_weight(self):
        return self.weight

    def get_serializable_doc(self):
        return {
            "doc_id": self.doc_id,
            "weight": self.weight,
            "positions": self.positions
        }
