class Car:
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price

    def identify_car(self):
        return f"{self.make} {self.model}"

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

# Creating car objects
car1 = Car("Toyota", "Camry", "Red", 24000)
car2 = Car("Honda", "Civic", "Blue", 22000)
car3 = Car("Ford", "Mustang", "Black", 35000)

# Using the methods
print(car1.identify_car())  # Output: Toyota Camry
print(car1.get_color())     # Output: Red
print(car1.get_price())     # Output: 24000

print(car2.identify_car())  # Output: Honda Civic
print(car2.get_color())     # Output: Blue
print(car2.get_price())     # Output: 22000

print(car3.identify_car())  # Output: Ford Mustang
print(car3.get_color())     # Output: Black
print(car3.get_price())     # Output: 35000

# Adding dunder methods
def __str__(self):
    return f"{self.make} {self.model} in {self.color} costs ${self.price}"

def __repr__(self):
    return f"Car(make='{self.make}', model='{self.model}', color='{self.color}', price={self.price})"

# Adding dunder methods to the class
Car.__str__ = __str__
Car.__repr__ = __repr__

# Testing dunder methods
print(car1)  # Output: Toyota Camry in Red costs $24000
print(repr(car2))  # Output: Car(make='Honda', model='Civic', color='Blue', price=22000)