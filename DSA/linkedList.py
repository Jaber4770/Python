""" 
A doubly linked list is implemented as a dictionary of dictionaries like, for example, the following: 

dll = { 'head': {'prev': None, 'next': 12},
12: {'prev': 'head', 'next': 24},
24: {'prev': 12, 'next': 37},
37: {'prev': 24, 'next': 14},
14: {'prev': 37, 'next': 3},
3: {'prev': 14, 'next': 'tail'},
'tail': {'prev': 3, 'next': None}}
Implement the Python function delete_first(dll) that removes the node 
closer to the head and returns the doubly linked list modified.

-solution? similar type question collect from chatgpt
"""