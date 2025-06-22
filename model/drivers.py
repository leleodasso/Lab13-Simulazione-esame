from dataclasses import dataclass
from datetime import datetime


@dataclass
class Driver:
    driverId: int
    driverRef: str
    number: int
    code: str
    forename: str
    surname: str
    dob: datetime
    nationality: str
    url: str

    def __eq__(self, other):
        return self.driverId == other.driverId

    def __hash__(self):
        return hash(self.driverId)