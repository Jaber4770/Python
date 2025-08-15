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
print('hello listt')