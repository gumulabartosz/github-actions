class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

car = Car("Toyota", "Corolla")
print(car.info())