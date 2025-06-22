from dataclasses import dataclass

@dataclass
class ConstructorStanding:
    constructorStandingsId: int
    raceId: int
    constructorId: int
    points: float
    position: int
    positionText: str
    wins: int

    def __eq__(self, other):
        return self.constructorStandingsId == other.constructorStandingsId

    def __hash__(self):
        return hash(self.constructorStandingsId)