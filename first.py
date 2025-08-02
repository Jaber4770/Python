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