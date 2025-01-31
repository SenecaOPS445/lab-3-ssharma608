#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: [seneca_id]


import lab3b

lab3b.sum_numbers(10, 5)
# Will return 15
lab3b.sum_numbers(25, 25)
# Will return 50
lab3b.subtract_numbers(10, 5)
# Will return 5
lab3b.subtract_numbers(5, 10)
# Will return -5
lab3b.multiply_numbers(10, 5)
# Will return 50
lab3b.multiply_numbers(10, 2)
# Will return 20

def operate(number1, number2, operator):
    if operator == 'add':
         return lab3b.sum_numbers(number1, number2) 
    elif operator == 'subtract': 
         return lab3b.subtract_numbers(number1, number2)
    elif operator == 'multiply':
         return lab3b.multiply_numbers(number1, number2)
    else:
         return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))
