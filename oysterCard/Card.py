
from oysterCard.ENUMS import Fares, Transport
from oysterCard.Journey import Journey
import time

class Card:



    MINIMUM_FARE = 1.8 # minimum fare to be charged as in table provided.

    def __init__(self) -> None:
        self.balance = 0.0
        self.charged_fare = 0.0
        self.journey = Journey
        self.journey_hist = []
        self.transport_mode = None
        self.swip_in = False
    

    def add_money(self, money_val):
        """_summary_

        Args:
            amount (_type_): _description_
        """
        if isinstance(money_val, float):
            self.balance += money_val
        else:
            raise ValueError("Money Amount must be float")
        return money_val


    def get_in(self, station, transport_mode):
        """_summary_

        Args:
            station (_type_): _description_
        """

        # in case the transport is BUS fare = 1.8
        # in case TUBE fare = MAX_COST till swipe_out in exit station

        self.charged_fare =  Fares.ANY_BUS if transport_mode == transport_mode.BUS  else Fares.MAX_COST 
        self.transport_mode = transport_mode
        self.swip_in = True

        if self.balance < self.charged_fare.value:
            raise RuntimeError("Balance doesn't meet the minimum fare!")
        
        self._deduct(self.charged_fare.value)

        self.journey.start_station = station
        self.journey.isin_journey = True

        return True


    def get_out(self, station=None):
        """_summary_

        Args:
            station (_type_): _description_
        """
        fare = 0
        if self.swip_in:
            if self.transport_mode == Transport.BUS:
                pass
            elif self.transport_mode == Transport.TUBE:

                self.journey.end_station = station

                self.journey_hist.append(self.journey)
                self.journey.isin_journey = False

                fare = self._calculate_possible_fares(self.journey, self.transport_mode)

                self._deduct(fare, replace=True)
        else:
            fare = Fares.MAX_COST

        return True, fare



    def _deduct(self, fare, replace=False):
        """_summary_

        Args:
            fare (_type_): _description_
        """
        if replace:
            self.balance += Fares.MAX_COST.value
            self.balance -= fare
        else:
            self.balance -= fare
        
        return self.balance



    def _calculate_possible_fares(self, journey, transport_mode):        
        possible_fares = []
        final_fare = 0

        if transport_mode == transport_mode.BUS:
            final_fare = Fares.ANY_BUS.value
        elif transport_mode == transport_mode.TUBE:

            entry_zone = self.journey.start_station.zone
            end_zone = self.journey.end_station.zone
            
            if isinstance(entry_zone, list) and isinstance(end_zone, list):
                for z1 in entry_zone:
                    for z2 in end_zone:
                        possible_fares.append(self._calculate_fare(z1, z2))
            elif isinstance(entry_zone, list) and isinstance(end_zone, int):
                for z1 in entry_zone:
                    possible_fares.append(self._calculate_fare(z1, end_zone))
            elif isinstance(entry_zone, int) and isinstance(end_zone, list):
                for z2 in end_zone:
                    possible_fares.append(self._calculate_fare(entry_zone, z2))
            
            print("Possible Fares are: ", possible_fares)
            final_fare = min(possible_fares)
            time.sleep(1)
            print("The system will favour the customer with fare: ", final_fare)
        return final_fare


    def _calculate_fare(self, entry_zone, end_zone):
        """_summary_

        Args:
            journey (_type_): _description_
        """

        # print("Start station: %s End Station %s " %(journey.start_station.name, journey.end_station.name))
        
        fare = 0
        if entry_zone == 1 and end_zone == 1:
            fare = Fares.ANYWHERE_IN_ZONE1.value
        elif entry_zone != 1 and end_zone != 1 and abs(entry_zone - end_zone) == 0:
            fare = Fares.ONEZONE_OUTSIDE_ZONE1.value
        elif entry_zone == 1 or end_zone == 1 and abs(entry_zone - end_zone) == 1:
            fare = Fares.TWO_ZONE_INCLUDING_ZONE1.value
        elif entry_zone != 1 and end_zone != 1 and abs(entry_zone - end_zone) == 1:
            fare = Fares.TWO_ZONE_EXCLUDING_ZONE1.value
        elif abs(entry_zone - end_zone) > 1:
            fare = Fares.THREE_ZONES.value

        return fare
        