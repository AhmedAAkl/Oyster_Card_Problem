import os, sys
from unittest import mock
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)



import unittest
from oysterCard.Station import Station
from oysterCard.ENUMS import StationZone
from oysterCard.Journey import Journey


class TestJourney(unittest.TestCase):

    def setUp(self):
        self.start = Station(StationZone.EARLS_COURT.value['name'], StationZone.EARLS_COURT.value['zone'])
        self.end = Station(StationZone.EARLS_COURT.value['name'], StationZone.EARLS_COURT.value['zone'])

    def test_journey_init(self):
        journey = Journey()


unittest.main()
