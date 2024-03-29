"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator_2():
    while True:
        calc = input("> ")          # get user input
        tokens = calc.split(" ")    # tokenize user input
        operator = tokens[0]        # identify the function to call
        # num1 = tokens[1]
        # num2 = tokens[2]
        # num3 = tokens[3]
        if operator == 'q':
            return
        elif operator == '+':
            answer = addition(int(tokens[1]), int(tokens[2]))
            # print(answer)
        elif operator == '-':
            answer = subtract(int(tokens[1]), int(tokens[2]))
        elif operator == '*':
            answer = multiply(int(tokens[1]), int(tokens[2]))
        elif operator == '/':
            answer = divide(int(tokens[1]), int(tokens[2]))
        elif operator == 'square':
            answer = square(int(tokens[1]))
        elif operator == 'cube':
            answer = cube(int(tokens[1]))
        elif operator == "pow":
            answer = power(int(tokens[1]), int(tokens[2]))
        elif operator == "mod":
            answer = mod(int(tokens[1]), int(tokens[2]))
        else:
            print('Invalid operator!')

        print(answer)


calculator_2()