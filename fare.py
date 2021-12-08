#Create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self, name, mileage, capacity): #class attributes
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self): #cost of 1 fare
        return self.capacity * 100

#Class Inheritance
class Bus(Vehicle): #a bus is a vehicle
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount #fare overridden


#result
Passenger_amt = input("Enter the amount of passengers: ")
School_bus = Bus("School Volvo", Passenger_amt) 
print("Total Bus fare is:", School_bus.fare())
