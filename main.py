import os
import unittest


fake_data = "1, 2, two, one"


def add_two_numbers(a: int, b: int) -> int:
    """Add two numbers

    Args:
        a (int): first argument
        b (int): second argument

    Returns:
        int: _description_
    """    
    return a + b


def parse_file(file_name: str) -> list:
    with open(file_name, "r") as f:
        data = f.read()
    
    result = [item.strip() for item in data.split(",")]
    
    return result


class TestMyFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_two_numbers(1, 1), 2, "Not Equal")
    
    def test_add_negative_number(self):
        self.assertEqual(add_two_numbers(-1, -1), -2)


class TestParser(unittest.TestCase):
    
    file_name = "data.txt"
    
    @classmethod
    def setUpClass(cls) -> None:
        with open(cls.file_name, "w") as f:
            f.write(fake_data)
    
    @classmethod
    def tearDownClass(cls) -> None:
        os.remove(cls.file_name)
        
    def setUp(self) -> None:
        print("Before call method")
    
    def tearDown(self) -> None:
        print("After call method")
    
    def test_type_parse(self):
        self.assertIsInstance(parse_file(self.file_name), list)
    
    def test_item_parse(self):
        self.assertEqual(parse_file(self.file_name)[1], "2")
    

if __name__ == '__main__':
    unittest.main()