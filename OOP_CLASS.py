# oop is call object oriented programming
# characterristics of an object
# object Attributes 
# object methods(functions)

# class car:
#     owner="john smith"
#     location="lagos"
#     gear=5
#     tire=4
#     engin="v6"
#     door=4
#     bonnet=True
#     boot=True
#     speed="500km/hr"

#     def run(self, value):
#         print("the car is running at the full speed of "+value+ "km/hr")
#         def pack():
#             print("the car just pack now.")

# my_car=car()
# my_car2=car()

# print(type(my_car))
# print(my_car.gear)
# my_car.run('35')
# my_car.location="ogbomoso"
# print(my_car.location)

# class car:
#     traffic=False
#     stirring=1

#     def __init__(self):
#         self.owner ="john brown"
#         self.location ="lagos"
#         self.gear ="5"
#         self.speed="550km/hr"
        
#         self.run("45")

#     def run(self, value):
#         value1= 4
#         self.gear=45
#         self.passenger= 12
#         print("the car is running with full speed of "+value+"km/hr")
#         self.pack()
    
#     def pack(self):
#         print("the car just pack now in "+self.location)
    # def reverse(self):
        # print("this car is reversing but it still in gear "+str(self.gear))

#     def drive(self):
#         print("the car is driving now")
# my_car = car()
# # print(my_car.traffic)
# my_car.drive()

# class car:
#     def __init__(self, owner,location='lagos'):
#         self.owner=owner
#         self.location=location
#         self.name="toyota"
#         self.color='red'
#         self.brand="2020 moodel"
#         self.trafficator="straight"
#         self.tyre=4
#         self.stirring=1
#         self.gear="0"

#         self.details("$10000")

#     def __init__(self):
#         self.owner="ruth abel"
#         self.location="uk"
#         self.name="toyota"
#         self.details("$10000")

#     def details(self, value):
#         print("this car is owned by "+self.owner+ "and is located in "+self.location)
#         print("this car is valued at "+value)

# toyota_camry=car("Ronke","canada")

import time
class car:
    def __init__(self):
        self.owner="john smith"
        self.location="lagos"
        self.name="toyota"
        self.color='red'
        self.brand="2020 model"
        self.trafficator="straight"
        self.tyre=4
        self.stirring=1
        self.gear="0"
        self.speed="10km/hr"
        
        self.details()

    def details(self):
            print("this car is owned by "+self.owner+ "and is located in "+self.location+'.\nThis car was built by'+self.name+"it is "+self.color+"and the brand is "+self.brand)
            time.sleep(2)
            self.startEngin()


    def startEngin(self):
        print("engin got started>>>>")
        time.sleep(2)
        self.gear=input("enter gear 1 to take off >>")
        if self.gear =='1':
            self.moveCar()
        else:
            print("that is not the right gear to take off with")
            self.startEngin()

    def moveCar(self):
        print(self.name+" is in gear "+self.gear+" and is moving "+self.trafficator+' at a speed of '+self.speed)
        self.drive=input("press Y to change gear, D to change direction, S to change speed and P to pack >>>>")
        if self.drive.upper()=="Y":
            self.changeGear()
        elif self.drive.upper()=="D":
            self.direction()
        elif self.drive.upper()=="S":
            self.changeSpeed()
        elif self.drive.upper()=="P":
            self.park()
        else:
            self.moveCar()

    def drive(self):
        print("the car is driving now")

    def changeGear(self):
        self.gear=input("enter gear number >>>")
        self.moveCar()

    def direction(self):
        self.trafficator=input("please enter your direction >>> ")
        self.moveCar()

    def changeSpeed(self):
        newSpeed=int(input('enter your new speed >>>'))
        if self.gear == "1" and newSpeed > 30:
            print("incompatible speed, gear must not be greater than 30 when on gear 1") 
            self.moveCar()
        elif self.gear == "2" and newSpeed > 60:
            print("incompatible speed, gear must not be greater than 60 when on gear 2")
            self.moveCar()
        elif self.gear == "2" and (newSpeed > 120 or newSpeed<60):
            print("incompatible speed, gear must be  between 60 and 120 when on gear 3")
            self.moveCar()

    def park(self):
        print("the car is packing now")
        time.sleep(2)
        print("the car is properly parked")
        
toyota_camry=car()
