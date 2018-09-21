import ship
import time
from ship import Ship

def Clear():
    print(chr(27) + "[2J")

print("Welcome to Star Adventure")

#You need to initialize the parts being used before you can use them
MyShip: Ship = ship.Ship()
#The sole purpose of this boolean is to have an infinite while that goes until you exit
#The way this is set up right now, this is the only way to exit the game 'correctly'
again = True
#You can add other ships, or station locations and access them from here
#Obviously you'll want to have your primary 'local' be here. I did a station as 'home base'
#with the idea that you would 'go out' on adventures, then return to the station between them
while(again):
    Clear()
    print("Places you can go:")
    print("1: My Ship")
    print("2: Exit Game")
    command = input("What action would you like to take?\n")
    if(command == "1"):
        MyShip.ShipAirlock()
    elif(command == "2"):
        again = False
        print("Thanks for playing Star Adventure!")
        time.sleep(5)

