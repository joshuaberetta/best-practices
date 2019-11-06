import app.hello_world
from app.hello_world import printing
import unittest

class TestPrinting(unittest.TestCase):

    def test_printing_string(self):
        try:
            printing('something')
        except:
            raise Exception('Something went wrong with the hello_world.printing function when printing a string.')

    def test_printing_int(self):
        try:
            printing(12345)
        except Exception as err:
            print('Exception: ', err)

