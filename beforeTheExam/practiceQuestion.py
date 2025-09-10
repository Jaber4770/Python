x = 15
y = 4
print(x // y)
print(x % y)


#---------------------------
for i in range(3):
    print(i * i)
#-----------------------------
a = [1, 2, 3]
a.append(4)
print(a)

#-----------------------------
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

#-----------------------------
text = "hello"
print(text[::-1])

#-----------------------------
for i in range(1,6):
    if i == 3:
        continue
    print(i)
#-----------------------------
a = 10
b =5
if a>b:
    print("greater")
else:
    print('smaller')
    
#-----------------------------
a = [10,20,30]
print(a[1])

#-----------------------------
for i in range(2,10,2):
    print(i, end=" . ")
    
#-----------------------------
x = '123'
print('\n', int(x) + 5)

#-----------------------------
i = 1
while i<5:
    print(i)
    i+=1
#-----------------------------
a = 10
b = 3
c = a *b
print(c)

#-----------------------------
lst = [1,2,3,4,5,6]
print(len(lst))

#-----------------------------
a = 'Python'
for ch in a:
    print(ch, end="-")
#-----------------------------
""" Write the Python function onlyodd(xlist), xlist being a list of 10 integers in the range (1,20),that returns a list containing only the odd numbers contained in the list xlist. """

def onlyodd(xlist):
    oddList = []
    for x in xlist:
        if x % 2 != 0:
            oddList.append(x)
    print(oddList)
    
xlist = [1,2,3,4,5,6,7,8,9,10]
onlyodd(xlist)

#-----------------------------
""" Write a function alternate_case(s) that returns the input string with characters in alternating upper and lower case, starting with uppercase. """
def alternate_case(s):
    txt = ''
    for i, char in enumerate(s):
        if i % 2 == 0:
            txt += char.upper()
        else:
            txt += char.lower()
            
    return txt 

s = 'the quick brown fox jumps over the laxy dog'
result = alternate_case(s)
print('result: ', result)

#-----------------------------
""" Write a function digit_sum(n) that recursively returns the sum of the digits of an integer n. """
def digit_sum(n):
    if n<10:
        return n
    else: 
        return n % 10 + digit_sum(n//10)
    
digit = 234
resultDigit = digit_sum(digit)
print('sum of the digit: ', resultDigit)

#-----------------------------
""" A doubly linked list is implemented as a dictionary of dictionaries like, for example, the following: 

dll = { 'head': {'prev': None, 'next': 12},
12: {'prev': 'head', 'next': 24},
24: {'prev': 12, 'next': 37},
37: {'prev': 24, 'next': 14},
14: {'prev': 37, 'next': 3},
3: {'prev': 14, 'next': 'tail'},
'tail': {'prev': 3, 'next': None}}
Implement the Python function delete_first(dll) that removes the node 
closer to the head and returns the doubly linked list modified. """

""" def delete_first(dll):
    first_node = dll['head']['next']
    second_node = dll[first_node]['next']
    
    dll['head']['next']= second_node
    dll[second_node]['prev']= 'head'

    del dll[first_node]
    return dll

dll = { 
'head': {'prev': None, 'next': 12},
12: {'prev': 'head', 'next': 24},
24: {'prev': 12, 'next': 37},
37: {'prev': 24, 'next': 14},
14: {'prev': 37, 'next': 3},
3: {'prev': 14, 'next': 'tail'},
'tail': {'prev': 3, 'next': None}
}

result_Dll = delete_first(dll)
print(result_Dll) """

#-----------------------------
""" A doubly linked list is implemented as a dictionary of dictionaries like, for example, the following: 

dll = { 'head': {'prev': None, 'next': 12},
12: {'prev': 'head', 'next': 24},
24: {'prev': 12, 'next': 37},
37: {'prev': 24, 'next': 14},
14: {'prev': 37, 'next': 3},
3: {'prev': 14, 'next': 'tail'},
'tail': {'prev': 3, 'next': None}}
Implement the Python function find_smallest(dll) that returns the smallest value 
stored in the doubly linked list. """
def find_smallest(dll):
    current = dll['head']['next']
    smallest = current
    
    while current != 'tail':
        smallest = current
        current = dll[current]['next']
    
    return smallest
    

dll = { 'head': {'prev': None, 'next': 12},
12: {'prev': 'head', 'next': 24},
24: {'prev': 12, 'next': 37},
37: {'prev': 24, 'next': 14},
14: {'prev': 37, 'next': 3},
3: {'prev': 14, 'next': 'tail'},
'tail': {'prev': 3, 'next': None}}

resultSmall = find_smallest(dll)
print("res: " ,resultSmall)

#-----------------------------
""" A binary tree is represented as a dictionary of dictionaries such as for example 

btree = { 'root':{'P':None, 'L': 1, 'R':10},
1:{'P':'root', 'L':5, 'R':3}, 10:{ 'P':'root', 'L':12, 'R':13},
5:{'P':1, 'L':None, 'R':None}, 3:{'P':1, 'L':None, 'R':None},
12:{'P':10, 'L':None, 'R':None}, 13:{'P':10, 'L':None, 'R':None}}

Implement the Python function in_order_search(btree, key) that traverses the binary tree using the in_order traversal algorithm and returns True if key is found, False otherwise.

 """
def in_order_search(btree, key):
    # Helper recursive function
    def helper(node):
        if node is None:
            return False  # reached a leaf
        
        # Traverse left subtree
        if helper(btree[node]['L']):
            return True
        
        # Check current node
        if node == key:
            return True
        
        # Traverse right subtree
        if helper(btree[node]['R']):
            return True
        
        return False  # key not found in this branch
    
    # Start traversal from the root
    return helper('root')


# Example usage:
btree = { 
    'root': {'P': None, 'L': 1, 'R': 10},
    1: {'P': 'root', 'L': 5, 'R': 3}, 
    10: {'P': 'root', 'L': 12, 'R': 13},
    5: {'P': 1, 'L': None, 'R': None}, 
    3: {'P': 1, 'L': None, 'R': None},
    12: {'P': 10, 'L': None, 'R': None}, 
    13: {'P': 10, 'L': None, 'R': None}
}

print(in_order_search(btree, 12))  # True
print(in_order_search(btree, 7))   # False


#i got mara on the exam today. 