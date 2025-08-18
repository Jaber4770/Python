aSet = {1,2,3,45}
bSet = {3,4,5,6,7,8,9}

numbers =[2,3,4,5]
nSet = set(numbers)
print(nSet)


emptySet = set()
print(emptySet)
EmptySet = {}
print(EmptySet)

print("Length of a set: ",len(aSet))
if 45 in aSet:
    print("the element", 45, "is contained in the set")
    


ca = {'red',"white"}
it = {"red","white","green"}
fr = {"red","white","bluee"}

if ca.issubset(it):
    print("subset")

if it == fr:
    print("the same color")
    
if ca != fr:
    print("not the same colors")


