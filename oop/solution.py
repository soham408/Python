# 1. Basic Class and Object Problem: Create a Car class with attributes like brand and model. Then create an instance of this

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):  
        # 4. Encapsulation Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
        return self.__brand + " !"
    

    def full_name(self):  # 2. Class Method and SelfProblem: Add a method to the Car class that displays the full name of the car (brand and model).
        return f"{self.brand} {self.model}"
    
    def fule_type(self):
        # 5. PolymorphismProblem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
        return "Petrol or Diesel"
    
class ElectricCar(Car):  # 3. Inheritance Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
    def __init__ (self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fule_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
print(my_tesla.fule_type())

safari = Car("Tata", "Safari")
print(safari.fule_type())

# print(my_tesla.__brand)
# print(my_tesla.get_brand())

# print(my_tesla.model)
# print(my_tesla.full_name())

# my_car = Car("Hyundai", "Creta diesel manual")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())
