class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air By Mother")


class Pickup(Vehicle):
    color = ""
    def PrintPickupColor (self):
        print("Pickup Color : " + self.color)

    #def turnOnAirConditioner(self):
        #print("Turn On : Air By Pickup")

pickup1 = Pickup()
pickup1.turnOnAirConditioner()
pickup1.color = "red"
pickup1.PrintPickupColor()

