#Skylar Thompson
#M03 Lab - Case Study: Lists, Functions, and Classes

class Vehicle():
    def __init__(self, type):
        self.type = type
        
    def __str__(self):
        return self.type

class Automobile(Vehicle):
    def __init__(self, Vehicle, year, make, model, doors, roof):
        self.Vehicle = Vehicle
        self.year = year
        self.make = make
        self.model = model 
        self.doors = doors 
        self.roof = roof 
    
        
    def __str__(self):
        autoData = '\n\nVehicle Type: {}\n' \
                    'Year: {}\n' \
                    'Make: {}\n' \
                    'Model: {}\n' \
                    'Number of Doors: {}\n' \
                    'Type of Roof: {}\n '.format(self.Vehicle, self.year, self.make, self.model, self.doors, self.roof)
        return autoData

#myTruck = Vehicle('whiteTruck')
#myTruckAuto = Automobile(myTruck.__str__(), 2014, 'Ford', 'F150', 4, 'Solid')

#print(myTruckAuto.__str__())

myVehicle = Vehicle(str(input("What Type of Vehicle do you have? (Car, Truck, Motorcycle, Etc): ")))

year = input("What is the Year of your {}? ".format(myVehicle.type))
make = input("What is the Make of your {}? ".format(myVehicle.type))
model = input("What is the Model of your {}? ".format(myVehicle.type))
doors = input("How many Doors does your {} have? ".format(myVehicle.type))
roof = input("Does your {} have a Solid or Sun Roof? ".format(myVehicle.type))

myAuto = Automobile(myVehicle, year, make, model, doors, roof)

print(myAuto)


