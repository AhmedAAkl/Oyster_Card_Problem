

from oysterCard.Card import Card
from oysterCard.ENUMS import Fares, Transport, StationZone
from oysterCard.Station import Station
import time


print("Charge the Oyster Card with 30 £.")
time.sleep(1)
card = Card()
card.add_money(30.0)
print("Card Balance: ", str(card.balance) + " £")
time.sleep(2)

print("------------------------------------------------------------------------------")
time.sleep(1)
print("Trip 1: From Tube Holborn to Earl’s Court")
station = Station(StationZone.HOLBORN.value['name'], StationZone.HOLBORN.value['zone'])
time.sleep(1)
print("The Customer swipe in at the Tube Holborn Station:")
time.sleep(1)
card.get_in(station, Transport.TUBE)
print("Card balance after charge the max cost: ", str(card.balance) + " £" )
time.sleep(2)
station = Station(StationZone.EARLS_COURT.value['name'], StationZone.EARLS_COURT.value['zone'])
card.get_out(station)
print("The Customer swipe out at the Earl's Court Station:")
time.sleep(1)
print("Current Balance after swipe out: ", str(card.balance) + " £" )
time.sleep(2)

print("------------------------------------------------------------------------------")
time.sleep(1)
print("Trip 2: 328 bus from Earl’s Court to Chelsea")
time.sleep(2)
print("The customer swipe in at the 328 bus station.")
station = Station(StationZone.EARLS_COURT.value['name'], StationZone.EARLS_COURT.value['zone'])
card.get_in(station, Transport.BUS)
time.sleep(1)
print("The Customer will charge only 1.8 £ for all bus journeys.")
station = Station('Chelsea', 0)
card.get_out(station)
time.sleep(1)
print("Card Balance: ", str(card.balance) + " £")
time.sleep(2)


print("------------------------------------------------------------------------------")
time.sleep(1)
print("Trip 3: From Tube Earl’s court to Hammersmith")
station = Station(StationZone.EARLS_COURT.value['name'], StationZone.EARLS_COURT.value['zone'])
time.sleep(1)
print("The customer swipe in at the Earl's Court Tube station.")
card.get_in(station, Transport.TUBE)
time.sleep(1)
print("Card balance after charge the max cost: ", str(card.balance) + " £" )
time.sleep(1)
station = Station(StationZone.HAMMERSMITH.value['name'], StationZone.HAMMERSMITH.value['zone'])
card.get_out(station)
print("The Customer swipe out at the Hammersmith Station:")
time.sleep(1)
print("The maximum fare transaction removed and replaced with the real transaction")
time.sleep(1)
print("Current Balance after swipe out: ", str(card.balance) + " £" )


time.sleep(2)

print("------------------------------------------------------------------------------")
