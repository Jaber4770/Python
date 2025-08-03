# 
""" A number a is power of b if it is divisible by b and if a/b is a
power of b. Write a function named power(a,b) which
requires two arguments (a and b) and returns True if a is a
power of b. """ 
def power(a, b):
    if a == 1:
        return True
    if a < b or a % b != 0:
        return False
    return power(a // b, b)

print(power(8,2))



""" Write the recursive function product(n) which requires an
integer number n as argument and returns its product with all
natural numbers that precede it. For example, product(4)
must return 24 = 4 · 3 · 2 · 1 """
def product(n):
    if(n<=0):
        return 1
    else: 
        return n * product(n-1)

print("from product: ",product(4))


# while loop
def countdown(n):
    while n>0:
        print(n)
        n-=1
        print('via!!!!')
countdown(5)

# another one
c = 5
while c<10 and c>=0:
    print('choto vai',c)
    c-=1


# 
def sequence(n):
    while n!=1:
        print(n, end=' → ')
        if n % 2 == 0:
            n = n//2
        else:
            n = n * 3 + 1
    print(n)

sequence(160)


# break
while True:
    line = input("enter a string: ")
    if line == "done":
        break
    print(line)
print("Done!")


import math

def greekpi():
    gpi, i = 0, 0
    while abs(gpi - math.pi) > 0.0001:
        gpi += 4 * math.pow(-1, i) / (2 * i + 1)
        print(i, gpi, abs(gpi - math.pi))  # Show step number, value, and error
        i += 1

    print("\nApproximation complete!")
    print(f"Approximated π: {gpi}")
    print(f"math.pi       : {math.pi}")
    print(f"Total terms   : {i}")

# Call the function
greekpi()

