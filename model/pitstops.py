from dataclasses import dataclass
from datetime import datetime


@dataclass
class Pitstop:
    raceId: int
    driverId: int
    stop: int
    lap: int
    time: datetime
    duration: str
    milliseconds: int

    def __eq__(self, other):
        return self.raceId == other.raceId and self.driverId == other.driverId and self.stop == other.stop

    def __hash__(self):
        return hash((self.raceId, self.driverId, self.stop))