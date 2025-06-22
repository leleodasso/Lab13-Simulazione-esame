from dataclasses import dataclass

@dataclass
class Circuit:
    circuitId: int
    circuitRef: str
    name: str
    location: str
    country: str
    lat: float
    lng: float
    alt: int
    url: str

    def __eq__(self, other):
        return self.circuitId == other.circuitId

    def __hash__(self):
        return hash(self.circuitId)