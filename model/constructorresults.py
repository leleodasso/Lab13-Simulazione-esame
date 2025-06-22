from dataclasses import dataclass

@dataclass
class ConstructorResult:
    constructorResultsId: int
    raceId: int
    constructorId: int
    points: float
    status: str

    def __eq__(self, other):
        return self.constructorResultsId == other.constructorResultsId

    def __hash__(self):
        return hash(self.constructorResultsId)