# miyad ye doc tarif mikone, vazne kalame too doco migire
# ye araye ham dare ke position-haye kalame too doc toosh save mishe
class Document:
    def __init__(self, weight, positions):
        self.weight = weight
        self.positions = positions

    def add_posting(self, pos):
        self.positions.append(pos)

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight
