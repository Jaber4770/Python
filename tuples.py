t1= 'a',
print(type(t1))
t2 =('2'),
print(type(t2))

t = tuple()
print(t)

t = tuple('ciaociao')
print(t)


# *arguments
def printAll(*args):
    print(args)
    
printAll("a","c","b")

remainderAndQuotient = (7,3)
result = divmod(*remainderAndQuotient)
print(result)


# zip function
a = 'abc'
b = [1,2,3]

result = zip(a,b)
print(result)

for i in zip(a,b):
    print(i)


# traversed
c = [("a",1),("b",2),("c",3)]
for let, num in c:
    print(let, num)
    # print(num,let)


""" Using zip and for it is possible to traverse two lists at the
same time """
def matches(t1,t2):
    for x,y in zip(t1,t2):
        if x==y:
            print('true')
    return print('false')

t1= "a","b","c"
t2= "1","3","c"
matches(t1,t2)


# enumerate
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))


# items
diz = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
t = diz.items()
print(t)
for k,v in diz.items():
    print(k,v)





