from dataclasses import dataclass

@dataclass
class Constructor:
    constructorId: int
    constructorRef: str
    name: str
    nationality: str
    url: str

    def __eq__(self, other):
        return self.constructorId == other.constructorId

    def __hash__(self):
        return hash(self.constructorId)