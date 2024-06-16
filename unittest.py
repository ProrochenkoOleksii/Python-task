# Task 1
# Choose your solution to one of the exercises in this module. Develop tests for this solution
# and write tests using the unittest library.

import unittest
import cw_25_11

class MyTest_addition(unittest.TestCase):
    def test_discount_func(self):
        res1=cw_25_11.discount_func(90)
        self.assertEqual(res1,(15.0,76.5))

if __name__ == '__main__':
    unittest.main()
    
# task 2
# Write tests for the Phonebook application you implemented in Module 1. Develop
# tests for this solution and write the tests using the unittest library
    
import unittest
import hw_15_11

class MyTest_addition(unittest.TestCase):
    def test_work_with_json (self):
        res=hw_15_11.work_with_json("alex")
        res_data=[{"1st name": "alex", "2nd name": "green", "full name": "alex green","phone number": 1234567, "city or state": "Rome"}]
        self.assertEqual(res,res_data)

    def test_work_with_json_2 (self):
        res2=hw_15_11.work_with_json("john")
        res_data2=[{'1st name': 'john', '2nd name': 'smith', 'full name': 'john smith', 'phone number': 2345678, 'city or state': 'Madrid'}]       
        self.assertEqual(res2,res_data2)


if __name__ == '__main__':
    unittest.main()
    
