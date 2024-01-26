# miyad ye doc tarif mikone, vazne kalame too doco migire
# ye araye ham dare ke position-haye kalame too doc toosh save mishe
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
