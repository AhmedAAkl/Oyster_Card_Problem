import os, sys
from unittest import mock
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)


import unittest
from oysterCard.Card import Card
from oysterCard.Station import Station
from oysterCard.ENUMS import StationZone, Transport, Fares
from unittest.mock import Mock
from oysterCard.Journey import Journey


class TestCard(unittest.TestCase):

    def setUp(self):
        self.mock_station = Mock()
        self.card = Card()

    def test_initial_balance_zero(self):
        self.assertEqual(self.card.balance, 0)

    def test_add_money_val_type(self):
        self.assertIsInstance(self.card.add_money(30.0), float)
    
    def test_add_money_increase_balance(self):
        self.assertEqual(self.card.add_money(30.0), 30.0)

    def test_add_money_wrong_val(self):
        with self.assertRaises(ValueError):
            self.card.add_money('wrong value')

    def test_deduct_decrease_balance(self):
        self.card.add_money(30.0)
        self.assertEqual(self.card._deduct(10.0), 20.0)

    def test_get_in_balance_is_not_sufficient(self):    
        self.card.add_money(1.0)
        with self.assertRaises(RuntimeError):
            self.card.get_in(self.mock_station, Transport.TUBE)
        

    def test_get_in_true(self):        
        self.card.add_money(20.0)
        self.assertTrue(self.card.get_in(self.mock_station,Transport.TUBE))



    def test_get_out_t(self):
        self.assertTrue(self.card.get_out(self.mock_station))

    def test_calculate_fare_between_zones(self):
        self.assertIn(self.card._calculate_fare(1,2), [2.50, 3.00, 2.00, 3.20, 2.25, 1.80])

    def test_possible_fares_between_zones(self):
        
        self.card.add_money(30.0)
        journey = Journey
        station = Station(StationZone.HOLBORN.value['name'], StationZone.HOLBORN.value['zone'])
        self.card.get_in(station, Transport.TUBE)
        station = Station(StationZone.EARLS_COURT.value['name'], StationZone.EARLS_COURT.value['zone'])
        _, fare = self.card.get_out(station)        
        self.assertIn(fare, [2.50, 3.00, 2.00, 3.20, 2.25, 1.80])


    def test_possible_fares_between_zones_many_zones(self):
        
        self.card.add_money(30.0)
        journey = Journey
        station = Station(StationZone.EARLS_COURT.value['name'], StationZone.EARLS_COURT.value['zone'])
        self.card.get_in(station, Transport.TUBE)
        station = Station(StationZone.EARLS_COURT.value['name'], StationZone.EARLS_COURT.value['zone'])
        _, fare = self.card.get_out(station)        
        self.assertIn(fare, [2.50, 3.00, 2.00, 3.20, 2.25, 1.80])

    def test_get_without_swipin(self):
        self.card.add_money(30.0)
        journey = Journey
        station = Station(StationZone.EARLS_COURT.value['name'], StationZone.EARLS_COURT.value['zone'])
        # self.card.get_in(station, Transport.TUBE)
        station = Station(StationZone.EARLS_COURT.value['name'], StationZone.EARLS_COURT.value['zone'])
        _, fare = self.card.get_out(station)       
        print("fare: ", fare)
        self.assertEqual(fare, Fares.MAX_COST)





unittest.main()

