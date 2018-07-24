import unittest
from triangle import *

class TestTriangleMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_valid_data_correct(self):
        self.assertEqual([1, 2, 3], get_valid_data("1,2,3"))
        self.assertEqual([2, 2, 3], get_valid_data("2,2,3"))
        self.assertEqual([3, 3, 3], get_valid_data("3,3,3"))
        self.assertEqual([10000, 10000, 10000], get_valid_data("10000,10000,10000"))
        self.assertEqual([55, 25, 3000], get_valid_data("55,25,3000,4000,144,5"))

    def test_get_valid_data_failer_length(self):
        message = 'must input 3 numbers.'
        with self.assertRaisesRegex(InputException, message):
            get_valid_data("1,2")
        with self.assertRaisesRegex(InputException, message):
            get_valid_data("1,")

    def test_get_valid_data_failer_character(self):
        message = 'must input integer number.'
        with self.assertRaisesRegex(InputException, message):
            get_valid_data("AAA,1,2")
        with self.assertRaisesRegex(InputException, message):
            get_valid_data("3,45,")
        with self.assertRaisesRegex(InputException, message):
            get_valid_data("872,98,")   
        with self.assertRaisesRegex(InputException, message):
            get_valid_data("987,1,678.01")   

    def test_get_valid_data_failer_length_range(self):
        message = 'number\'s range is 1-10000.'
        with self.assertRaisesRegex(InputException, message):
            get_valid_data("4,9,10001")
        with self.assertRaisesRegex(InputException, message):
            get_valid_data("0,809,77")
    
    def test_evaluate_correct(self):
        self.assertEqual("scalene", evaluate([10000,244,1]))
        self.assertEqual("isosceles", evaluate([10000,244,10000]))
        self.assertEqual("isosceles", evaluate([1,1,245]))
        self.assertEqual("isosceles", evaluate([9,67,67]))
        self.assertEqual("equilateral", evaluate([1,1,1]))
        self.assertEqual("equilateral", evaluate([10000,10000,10000]))

    def test_evaluate_failer_range(self):
        with self.assertRaises(Exception):
            evaluate([1,2])
        with self.assertRaises(Exception):
            evaluate([5,8,19,3])
            
if __name__ == '__main__':
    unittest.main()    