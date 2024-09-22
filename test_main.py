import unittest
from main import hello_world, greet_person, name


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, from Nashid!")

class TestGreeting(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greet_person(name), f"Hello, {name}!")

if __name__ == '__main__':
    unittest.main()