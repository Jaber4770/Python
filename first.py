msg = 'Hello World!'
pippo = 4.0
pluto =12

print(msg,pippo,pluto)

gradi = 360
pi = 3.14159
print(gradi/2*pi)
print(gradi /2/pi)

# this is comment, for single line comment
''' we can write multile line comment 
using triple single quotes'''

"""we can use double quotes also for multi line 
codes"""

print("-------------------------------------------------")

# convertion function, integer
value1 = int('32')
value2 = int(12.443)
print(value1, value2)

# text = int('sdlfdsjflo') this line will occur error, here i tried to conver alphabet to number which is not possible. 
# print(text)
print("-------------------------------------------------")
# float number converstion
print(float(23))
print(float('234'))

print("----------------------str---------------------------")
convertedText = str(23)
print(convertedText)
print(str('324.324'))


print("---------------------math----------------------------")
import math
unknownValue = math.cos(math.pi)
print(unknownValue)
print(math.pi, math.cos)

print("-------------------def func------------------------------")
def printing():
    print("print the first message")
    print("now print the second message")
printing()
print(printing())
print(printing)


print("------------------check type-------------------------------")
print(type(printing))
print(type(value1))
print(type(2.3554))

print("------------------------perameter and arguments-------------------------")
def printing2(argument1, argument2):
    print(argument1)
    print(argument2)

printing2(1,2)


def print3(argument1,argument2):
    x = argument1 + argument2
    print(x)

print3(2,2)

# we can not access local varialbe outside of a function
# print(x)

# void function, void means which is not return

def printing():
    print('1st msg')
    print('2nd msg')

result = printing()

print(result)

minutes = 105
a = minutes // 60
print(a)

remainder = minutes % 60
print("remaining minutes: ", remainder)


print(5==5)
print(5==6)
# print(5=5) syntax error

print(type(True))
print(type(False))


stringx = ' '
if(stringx):
    print('non empty')
else: 
    print('empty')



# else if: elif
a = 5
b = 4
if a>b:
    print('a is greater than b')
elif a<b:
    print('a is less than b')
else:
    print('a equal to y')

# nested
if a>b:
    if a<10:
        print("a is greater than b and less than 10")


# logical operators
if a>0 and a<10:
    print('a is positive and one figure')


# recursion
def countdown(n):
    if n<= 0:
        print('Go!!!')
    else:
        print(n)
        countdown(n-1)


# infinityy recurrtion
def inifinity_recurtion():
    print('Here we are...')
    inifinity_recurtion()
    

# input
# x1 = input()
# print("from print: ",x1)

# x2 = input("Enter an integer number\n")
# print(x2)


# datum = input("Enter an integer number\n")
# str = datum + 'xxxx'
# print(str)
# print(datum + '2')


# factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        x = factorial(n-1)
        result = n * x
        return result

print(factorial(5))


# fruitful functions
# recurtion

def factoriall(n):
    spaces = ' ' * (4 * n)
    print(spaces, 'Factorial', n)
    
    if n == 0:
        print(spaces, 'return 1')
        return 1
    
    else:
        ricors = factoriall(n-1)
        result = n * ricors
        print(spaces, "return", result)
        return result
        
factoriall(5)