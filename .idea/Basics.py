# Print hello world to the console
print("hello world")

#Store it in a variable first
allo = "Hello world"
print(allo)

#Return string by function
def printstring(string):
    print(string)

#Return string
def addition(num1, num2):
    return num1 + num2

#Conditionals
def additional(num1, num2, bool):
    if(bool == True):
        return num1+num2
    else:
        return num1*num2

#Condtionals 2
def additionals(num1, num2, bool):
    if(num1 == 0 or num2 == 0):
        return num1+num2
    elif(bool == True):
        return num1+num2
    else:
        return num1*num2

#Recursion
def recursion():
    for i in range(0, 10):
        print(additionals(10, i, True))

#Lists
def lists():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for number in numbers:
        print(additionals(number, 10, True))

#Lists/recursion
def listrecur():
    for number in numbers:
        print(number)

#Lists/recursion 2
emptylist = []

def listrecur2(length):
    for i in range(1, length+1):
        emptylist.append(i)
    print(emptylist)

def listtimesten(intList):
    for number in intList:
        print(number*10)

#User Input, commented out so I dont have to bother typing into console
# userlength = input('Specify a list length\n')
# listrecur2(int(userlength))

#Partial functions
from functools import partial

def partiallyapplied(x, y):
    return x*y

double = partial(partiallyapplied, 2)
triple = partial(partiallyapplied, 3)

def bj(num1, num2):
    if((num1 == 0 and num2 == 0) or (num1 > 21 and num2 > 21)):
        return 0
    elif(num1 == 0 and num2 <= 21):
        return num2
    elif(num2 == 0 and num1 <= 21):
        return num1
    elif((num1 >= num2 or num2 >= 21)and num1 <= 21):
        return num1
    elif((num2 >= num1 or num1 >= 21) and num2 <= 21):
        return num2

def uniquesum(one, two, three):
    if(one == two and two == three):
        return 0
    elif(one == two):
        return three
    elif(two == three):
        return one
    elif(one == three):
        return two
    else:
        return one*two*three

def leap(year):
    if(year %4 == 0 and (year %400 == 0 or year %100 != 0)):
        return True
    else:
        return False
