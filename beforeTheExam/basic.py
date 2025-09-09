print("hello exam!")

import sys
print(sys.version)

if 5>2:
    print("Hello exam, iam being prepared!")


x = 5
y = 'hello exam!'

# single line comment
""" multitle comment """

#variable
a,b,c = 'a','b','c'
print(a,b,c)

aa = 'hello exam, i am comming'
print(aa)

#list
fruits = ["banana", "apple", "cherry"]
print(fruits)

p = 'python is awesome'
print(p)

pp = 'python'
yy = 'is'
aaa = 'awesome'
print( pp + " " + yy +" "+ aaa)


#global variable
globalVariable = 'its a global variable'
def func(globalVariable):
    print(globalVariable)
    
func(globalVariable)

#--------------------------------type------------------------
def checkType():
    a = 'hello'
    b = 20
    c = 20.5
    d = 1j
    e = ['apple','ball']
    f = ('apple', 'banana')
    g = range(5)
    h = {'nam': 'jack', 'age': 23}
    i = {'lili', 'sunflower'}
    j = frozenset({'apple', 'banana', 'cherry'})
    k = True
    l = b'hello'
    m = bytearray(5)
    n = memoryview(bytes(5))
    o = None
    
    print(type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(h),type(i),type(j),type(k),type(l),type(m),type(n),type(o))
    
checkType()

#-------------convert ---------------------
def convertion():
    x = 1
    y = 1.8
    z = 1j
    
    a = float(x)
    b = int(y)
    c = complex(z)
    print(a,b,c)
    print(type(x), type(y), type(z), type(a), type(b), type(c))
    
convertion()


#random
import random

print(random.randrange(1,10))

#multile line string
sttring = """ hello 
tthis is
multie
line
string"""
print(sttring)

#character
def characcter():
    a = "hello exam!"
    print(a[1])
    
characcter()


for x in 'bananana':
    print(x)


banana = 'bananannana'
print(len(banana))

print(range(3))

txt = "The best things in life are free!"
if "free" in txt:
    print("yes! 'free' is presented")
    
#slice
texxt = 'Hello, Exam@!'
print(texxt[2:4])

upperText = 'hello Exam'
print(upperText.upper())
print(upperText.lower())

#remove white pace
def removeWhiteSpace():
    a = " Hello Exam I am  Comming Bro!"
    print(a)
    print(a.strip())
    print(a.replace("H", "J"))
    
removeWhiteSpace()
    