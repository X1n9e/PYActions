import unittest
from main import add_numbers

class Test(unittest.TestCase):
    def test_add_numbers(self):
        self.asserEqual(add_numbers(1,55),56)
        self.asserEqual(add_numbers(0,0),0)
        self.asserEqual(add_numbers(1,-5),4)


if __name__ == "__main__":
    unittest.main()
    
