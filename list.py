# ---------------------------------list--------------------------------------
la = ['hello', 'everyone', 'how', 'are', 'you', True, 344]
print(id(la))

secondIndex = la[3]
print(secondIndex)

la[2]= "How"
print(la)

for i in la:
    print(i)

# we can access item from last, using negative counts
getItemFromBackWard = la[-2]
print("getItemFromBackWard: ",getItemFromBackWard)


for i in range(len(la)):
    print(i+1,'\t',la[i])



lb= [1,3,4,5,6]
lc = [2,4,6,8]
print(lb+lc)
print(2*lc)


#  insert in list
listA = [1,2,3,4,5]
listA.insert(0,11)
print(listA)
listA.insert(2,555)
print(listA)
print('hello listt')

# reverse
listA.reverse()
print(listA)
listA.extend(lb)
print(listA)

# sort
listA.sort()
print(listA)

""" # Implement the Python function myreduce(a) that returns
the sum of the elements of the list a. """
def sum_list(s):
    sum = 0
    for x in s:
        sum += x
    return sum

a = [10,20,30,40]
print(sum_list(a))
print(sum(a))


# capitalized first letter
def capitalized_all(s):
    result = []
    for x in s:
        result.append(x.capitalize())
    return result

a = ["hello", "how", "are", "you"]
print(capitalized_all(a))


# only upper case
def only_upper(s):
    result = []
    for x in s:
        if x.isupper():
            result.append(x)
    return result

a = ["How", 'how', 'are', 'You?']
print(capitalized_all(a))
print("all character are capitalized: ",only_upper(a))



""" Implement the Python function mymap(a) that returns a list
containing the elements of the list a each multiplied by 2. """


def mymap(a):
    result = []              # create an empty list
    for b in a:              # go through each item in the list
        result.append(b * 2) # multiply by 2 and add to result
    return result            # return the new list

c = [1, 2, 3]
print(mymap(c))   # [2, 4, 6]



""" Implement the Python function myfilter(a) that returns a
list containing the odd elements of the list a each multiplied
by 2. """

def myfilter(a):
    oddItem = []
    for b in a:
        oddItem.append(b*2)
    return oddItem

k = [1,3,5]
print(myfilter(k))





lista = [1,2,3]
x = lista.pop(0)
print(x)
print(lista)

fox = 'the quick brown fox jumps over the laxy dog..'
s = list(fox)
print(fox)
print(s)
print(fox.split())
print(fox.split("a"))

# is
s1 = 'hello'
s2 = 'hello'
print(s1 is s2)

print(id(s1))
print(id(s2))
print(id(s1)==id(s2))

a1 = [1,2,3,4,5]
a2 = [1,2,3,4,5]
print(a1 == a2)
print(id(a1) )
print(id(a2))
print(id(a1) == id(a2))

print('----------------------------------')

d = [1,2,3,4,5]
print(d)
print(id(d))
def truncate(listd):
    listd.pop()
    
truncate(d)
print(d)
print(id(d))

print('-------------------------')

def bad_truncate(listx):
    listx = listx[1:]
    print('inside the fuction: ', listx)
    print(id(listx))

e = [100,10,20,30,40]
print(id(e))
bad_truncate(e)
print(id(e))
print('in the main: ', e)


print('-----------calculating the value of pi--------------')
import math
import random

def greekpi(eps):
    gpi = 0.0
    no_inside_points = 0
    no_total_points = 0
    
    while abs(gpi - math.pi)>eps:
        no_total_points +=1
        x = random.random()
        y = random.random()
        if (x**2 + y**2)<=1.0:
            no_inside_points +=1
        gpi = 4 * no_inside_points/no_total_points
        
    print("inside: ", no_inside_points,"total: ", no_total_points)
    print(gpi)
    print(math.pi)
    

greekpi(0.000001)



