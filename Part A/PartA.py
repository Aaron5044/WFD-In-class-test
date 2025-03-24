
class House:
    def __init__(self, house_number, street, area, num_beds, price):
        self.house_number = house_number
        self.street = street
        self.area = area
        self.num_beds = num_beds
        self.price = price

    def show_details(self):
        print("House Details:")
        print("House Number:", self.house_number)
        print("Street:", self.street)
        print("Area:", self.area)
        print("Number of Beds:", self.num_beds)
        print("Price:", self.price)
        print()

    def update(self, attr, value):
        if attr == "house_number" and isinstance(value, int):
            self.house_number = value
        elif attr == "street" and isinstance(value, str):
            self.street = value
        elif attr == "area" and isinstance(value, str):
            self.area = value
        elif attr == "num_beds" and isinstance(value, int):
            self.num_beds = value
        elif attr == "price" and isinstance(value, (int, float)):
            self.price = value
        else:
            print("Invalid update")

class Apartment(House):
    def __init__(self, house_number, street, area, num_beds, price, floor, has_elevator):
        super().__init__(house_number, street, area, num_beds, price)
        self.floor = floor
        self.has_elevator = has_elevator

    def show_details(self):
        super().show_details()
        print("Floor:", self.floor)
        print("Has Elevator:", self.has_elevator)
        print()

    def update(self, attr, value):
        if attr == "floor" and isinstance(value, int):
            self.floor = value
        elif attr == "has_elevator" and isinstance(value, bool):
            self.has_elevator = value
        else:
            super().update(attr, value)

# Creating instances
house_one = House(1, "Ratoath", "Ireland", 2, 150000)
apartment_one = Apartment(2, "Kollam", "India", 2, 5000, 5, True)

# Showing details
house_one.show_details()
apartment_one.show_details()

# Updating attributes
house_one.update("price", 320000)
house_one.update("num_beds", 4)
apartment_one.update("floor", 6)
apartment_one.update("has_elevator", False)

# Showing updated details
print("Updated Details:")
house_one.show_details()
apartment_one.show_details()
