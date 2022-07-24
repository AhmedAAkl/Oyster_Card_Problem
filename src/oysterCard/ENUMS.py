import enum


class Fares(enum.Enum):

    MAX_COST = 3.2
    ANYWHERE_IN_ZONE1 = 2.5
    ONEZONE_OUTSIDE_ZONE1 = 2.0
    TWO_ZONE_INCLUDING_ZONE1 = 3.0
    TWO_ZONE_EXCLUDING_ZONE1 = 2.25
    THREE_ZONES = 3.2
    ANY_BUS = 1.8    


class Transport(enum.Enum):
    BUS = "BUS"
    TUBE = "TUBE"


class StationZone(enum.Enum):

    HOLBORN = {'name': "HOLBORN", 'zone': 1}
    EARLS_COURT = {'name': "EARLS_COURT", 'zone': [1,2]}
    WIMBLEDON = {'name': "WIMBLEDON", 'zone':3}
    HAMMERSMITH = {'name': "HAMMERSMITH", 'zone':2}


