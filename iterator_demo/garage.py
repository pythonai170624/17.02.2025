class Car:
    def __init__(self, brand, model, year, price, color):
        """Initialize the car with basic attributes."""
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.color = color

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.year} {self.color} {self.brand} {self.model} {self.price}"

    def __repr__(self):
        """Return a string representation of the car."""
        return f"{self.year} {self.color} {self.brand} {self.model} {self.price}"

class Garage:
    def __init__(self):
        self.cars = []
        self.current = 0

    def add_car(self, car, *cars):
        self.cars.extend([car, *cars])

    def __iter__(self):
        return self  # The iterator itself

    def __next__(self):
        if self.current >= len(self.cars):
            self.current = 0
            raise StopIteration
        value = self.cars[self.current]
        self.current += 1
        return value

    def reset(self):
        self.current = 0

    # basic
    # def __getitem__(self, index):
    #     return self.cars[index]

    # by year
    # def __getitem__(self, year):
    #     result = [car for car in self.cars if car.year == year]
    #     return result

    # by year + *args
    def __getitem__(self, *args):
        result = [car for car in self.cars if car.year in list(*args)]
        return result

    def __str__(self):
        """Return a string listing all cars in the garage."""
        return "\n".join(str(car) for car in self.cars) if self.cars else "Garage is empty."

    # **BONUS
    def get_car(self, **kwargs):
        """Find cars by keyword arguments like brand, model, or year."""
        return [car for car in self.cars if all(getattr(car, k, None) == v for k, v in kwargs.items())]

shlomo6 = Garage()
car1 = Car("Toyota", "Camry", 2023, 28000, "White")
car2 = Car("Honda", "Civic", 2022, 25000, "Blue")
car3 = Car("Ford", "Mustang", 2024, 55000, "Red")
car4 = Car("Tesla", "Model 3", 2023, 42000, "Black")
car5 = Car("BMW", "X5", 2023, 65000, "Gray")
car6 = Car("Tesla", "Model 5", 2025, 44000, "Green")
shlomo6.add_car(car1, car2, car3, car4, car5)
print('-------- iter1 ')
for car in shlomo6:
    print(car)
print('-------- iter2 ')
# shlomo6.reset()
for car in shlomo6:
    print(car)

# print('shlomo6[0]', shlomo6[0])  # num index
# print('shlomo6[2023]', shlomo6[2023])  # num index
print('shlomo6[2023]', shlomo6[2023, 2024])  # num index
print('kwargs')
print(shlomo6.get_car(color='Red'))
# balance = b1 + b2


class Even:

    def __getitem__(self, number):
        return number % 2 == 0

even = Even()
print(even[5])