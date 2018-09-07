"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# add, subtract, multiply, divide, square, cube, power, mod


# Your code goes here


from functools import reduce

# create new list with each "token" as new index
def cal2():

    # while the answer is valid: 
        # execute everything 

    while True: 

        inpt = input("Enter operation  and numbers ").lower()
        inpt_splitting =  inpt.split(" ")

        if inpt_splitting == ['q']:
            print("Thank you for playing")
            break

        elif inpt_splitting[0] == '+':
            print(add(int(inpt_splitting[1]),int(inpt_splitting[2])))
        # 

        elif inpt_splitting[0] == '-':
            print(subtract(int(inpt_splitting[1]),int(inpt_splitting[2])))
        # 

        elif inpt_splitting[0] == '*':
            print(multiply(int(inpt_splitting[1]),int(inpt_splitting[2])))
        # 

        elif inpt_splitting[0] == '/':
            print(divide(int(inpt_splitting[1]),int(inpt_splitting[2])))
        # 

        elif inpt_splitting[0] == 'square':
            print(square(int(inpt_splitting[1])))
        # 


        elif inpt_splitting[0] == 'cube':
            print(cube(int(inpt_splitting[1])))
        # 

        elif inpt_splitting[0] == 'pow':
            print(power(int(inpt_splitting[1]),int(inpt_splitting[2])))
        # 

        elif inpt_splitting[0] == 'mod':
            print(mod(int(inpt_splitting[1]),int(inpt_splitting[2])))

        #otherwise, 
cal2()
    