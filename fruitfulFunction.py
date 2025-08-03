import math

def area (radius):
    a = math.pi * radius ** 2
    return a
    
print(area(2))

# shortcut

def areaa(radius):
    return math.pi * radius **2

print(areaa(5))

# multiple return

def absolute_Value(x):
    if x<0:
        return -x
    else:
        return x
    
print(absolute_Value(-2))


# function can return Boolean values also

def divisible(x,y):
    if x%y== 0:
        return True
    else:
        return False
print(divisible(2,3))


# test
def check(x,y,z):
    if(x<= y<=z):
        return True
    else:
        return False

print(check(3,4,5))


# checking arguments type

def factorial(n):
    if not isinstance(n, int):
        print("enter an integer number")
        return None
    elif n < 0:
        print('enter a positive integer number')
        return None
    elif n==0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input('enter a integer number: '))
print(factorial(n))






