import unittest

# House Class
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

# Apartment Class (Child Class)
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

# Unit Test Class
class TestHouse(unittest.TestCase):

    # B2: Test if an object is an instance of a class
    def test_house(self):
        house_one = House(1, "Ratoath", "Ireland", 2, 150000)
        self.assertIsInstance(house_one, House)
        print("Test Passed: test_house")

    # B3: Test if an object is NOT an instance of a class
    def test_apartment(self):
        house_one = House(1, "Ratoath", "Ireland", 2, 150000)
        self.assertNotIsInstance(house_one, Apartment)
        print("Test Passed: test_apartment")

    # B4: Test if 2 objects are identical
    def test_identical(self):
        house_one = House(1, "Ratoath", "Ireland", 2, 150000)
        house_two = House(1, "Ratoath", "Ireland", 2, 150000)
        self.assertEqual(house_one.house_number, house_two.house_number)
        self.assertEqual(house_one.street, house_two.street)
        self.assertEqual(house_one.area, house_two.area)
        self.assertEqual(house_one.num_beds, house_two.num_beds)
        self.assertEqual(house_one.price, house_two.price)
        print("Test Passed: test_identical")

    # B5: Unit test for update method
    def test_update_house(self):
        house_one = House(1, "Ratoath", "Ireland", 2, 150000)
        house_one.update("price", 18000)
        self.assertEqual(house_one.price, 18000)
        house_one.update("num_beds", 4)
        self.assertEqual(house_one.num_beds, 4)
        house_one.update("area", "London")
        self.assertEqual(house_one.area, "London")
        house_one.update("house_number", 102)
        self.assertEqual(house_one.house_number, 102)
        print("Test Passed: test_update_house")

    # B6: Unit test for Apartment class's update method
    def test_update_apartment(self):
        apartment_one = Apartment(2, "Kollam", "India", 2, 5000, 5, True)
        apartment_one.update("floor", 6)
        self.assertEqual(apartment_one.floor, 6)
        apartment_one.update("has_elevator", False)
        self.assertEqual(apartment_one.has_elevator, False)
        print("Test Passed: test_update_apartment")

    # B7: Run all tests
    def run_tests():
        unittest.main(argv=[''], exit=False)
        print("Test Passed: All test")
        

# Run tests
if __name__ == "__main__":
    TestHouse.run_tests()

