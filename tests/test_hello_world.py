import app.hello_world
from app.hello_world import printing, sum_nums
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


class TestSumNums(unittest.TestCase):

    def test_summing_ints(self):
        self.assertEqual(6.0, sum_nums([1,2,3]))

    def test_summing_floats(self):
        self.assertEqual(6.0, sum_nums([1.,2.,3.]))

    def test_summing_ints_and_floats(self):
        self.assertEqual(6.0, sum_nums([1.,2,3]))

    def test_summing_strings(self):
        try:
            sum_nums([1,2,3])
        except Exception as err:
            print('Exception: ', err)




