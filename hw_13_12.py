# Завдання 1
# Виберіть своє рішення до однієї із вправ цього модуля. Розробіть тести для цього рішення 
# та напишіть тести за допомогою бібліотеки unittest. 

# import unittest
# import cw_25_11

# class MyTest_addition(unittest.TestCase):
#     def test_discount_func(self):
#         res1=cw_25_11.discount_func(90)
#         self.assertEqual(res1,(15.0,76.5))

# if __name__ == '__main__':
#     unittest.main()
    


# завдання 2
# Напишіть тести для програми Phonebook, яку ви реалізували в модулі 1. Розробіть 
# тести для цього рішення та напишіть тести за допомогою бібліотеки unittest
    
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
    