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


lista = [1,2,3]
x = lista.pop(0)
print(x)
print(lista)





""" Implement the Python function mymap(a) that returns a list
containing the elements of the list a each multiplied by 2. """




""" Implement the Python function myfilter(a) that returns a
list containing the odd elements of the list a each multiplied
by 2. """