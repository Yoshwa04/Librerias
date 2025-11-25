from dict import techdex


class Technique:
    def __init__(self, nTechdex: str):
        self.techdex = nTechdex
        self.name = techdex[nTechdex]["name"]
        self.type = techdex[nTechdex]["type"]
        self.category = techdex[nTechdex]["category"]
        self.accuracy = techdex[nTechdex]["accuracy"]
        self.pp_max = techdex[nTechdex]["pp"]
        self.power = techdex[nTechdex]["power"]
        self.secondary_effects = techdex[nTechdex]["secondary_effects"]