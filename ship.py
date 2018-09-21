import time
class Ship:
    'Common base for all ships'
    def __int__(self, name):
        self.name = name

    def Clear(self):
        print(chr(27) + "[2J")

    openedCrates = 0

    #I added the opening a crate to show it's possible to add interaction
    #You could call another function instead of printing something
    #For example, OpenCrate() may give you a random chance of finding a spare part or something
    def ShipCargo(self):
        self.Clear()
        print("You're in the cargo bay.")
        print("You can perform the following actions:")
        print("1: Get on the Elevator")
        print("2: Open a crate")
        print("3: See how many crates you've opened")
        command = input("What action would you like to take?\n")
        if(command == "1"):
            self.ShipElevator()
        elif(command == "2"):
            print("You opened a crate.")
            self.openedCrates += 1
            self.ShipCargo()
        elif(command == "3"):
            print(f"You have opened {self.openedCrates} crates.")
            self.ShipCargo()
        else:
            self.ShipCargo()

    #This is just somewhere that controls access to different functions
    #Use this for navigation management
    #You could also have other areas connect differently
    #Such as having two staff quarters on a floor, so you go from staff quarters 1 to 2 OR to elevator
    def ShipElevator(self):
        self.Clear()
        print("You're in the Elevator.")
        print("You can perform the following actions:")
        print("1: Get off at the Bridge")
        print("2: Get off at the Cargo Bay")
        print("3: Get off at the AirLock (Get off the ship)")
        command = input("What action would you like to take?\n")
        if (command == "1"):
            self.ShipBridge()
        elif (command == "2"):
            self.ShipCargo()
        elif (command == "3"):
            self.ShipAirlock()
        else:
            self.ShipElevator()

    def ShipBridge(self):
        self.Clear()
        print("You're in the Bridge.")
        print("You can perform the following actions:")
        print("1: Get on the Elevator")
        print("2: Look out the window")
        command = input("What action would you like to take?\n")
        if (command == "1"):
            self.ShipElevator()
        elif (command == "2"):
            print("You look out the window and see an amazing array of stars in every visible direction.")
            print("The vast void filled with innumerable pricks of light makes you feel...\n...\n...")
            self.ShipBridge()
        else:
            self.ShipBridge()
    #A control point, short of a crash of some sort, this is the only place to leave the ship
    def ShipAirlock(self):
        self.Clear()
        print("You're in the Airlock")
        print("You can perform the following actions:")
        print("1: Get on the Elevator")
        print("2: Enter the station")
        command = input("What action would you like to take?\n")
        if (command == "1"):
            self.ShipElevator()
        elif (command == "2"):
            print("You leave the ship and head back to the station.")
            #Sleep for a few seconds to read the message
            #This could be used to give a timer to certain actions
            time.sleep(3)
        else:
            self.ShipAirlock()