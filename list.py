# ---------------------------------list--------------------------------------
la = ['hello', 'everyone', 'how', 'are', 'you', True, 344]
print(id(la))

secondIndex = la[2]
print(secondIndex)

la[2]= "How"
print(la)

# we can access item from last, using negative counts
getItemFromBackWard = la[-2]
print("getItemFromBackWard: ",getItemFromBackWard)