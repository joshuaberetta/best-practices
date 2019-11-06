import app.hello_world
from app.hello_world import printing, sum_nums, split_items
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


class TestSplitItems(unittest.TestCase):

    def test_splitting_string_of_ints_delim_space(self):
        tester:str = '1 2 3 4 5 6 7 8 9 10'
        split_on = ' '
        self.assertEqual(tester.split(split_on), 
                    split_items(tester, split_on))

    def test_splitting_string_of_strings_delim_space(self):
        tester:str = 'a b c d e f g h i j'
        split_on = ' '
        self.assertEqual(tester.split(split_on), 
                    split_items(tester, split_on))

    def test_splitting_string_of_strings_delim_uscore(self):
        tester:str = 'a_b_c_d_e_f_g_h_i_j'
        split_on = '_'
        self.assertEqual(tester.split(split_on), 
                    split_items(tester, split_on))

    def test_splitting_string_of_strings_delim_missing(self):
        tester:str = 'a_b_c_d_e_f_g_h_i_j'
        split_on = ' '
        try:
            self.assertEqual(tester.split(split_on), 
                        split_items(tester, split_on))
        except Exception as err:
            print('Exception: ', err)
        

    





