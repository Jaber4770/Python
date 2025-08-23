# -------------------------------------------------------------------------
def prefix_averagel(s):
    n = len(s)
    A = [0]*n
    for j in range(n):
        total = 0 
        for i in range(j+1):
           total += s[i]
        A[j] = total / (j + 1)
    return A
           
arrr = [1,2,3,4,5,6]
res = prefix_averagel(arrr)
print(res)

#--------------------------------------------------
def PrefixAvarage(list):
    n = len(list)
    newList = [0]*n
    for i in range(n):
        total = 0
        for j in range(i+1):
            total += list[j]
        newList[i]= total / (i+1)
    return newList

listt = [1,2,3,4,5,6,7,8,9]
ress = PrefixAvarage(listt)
print(ress)


# ------------------------------------------------
# another style to impliment aprefix avarrage
def prefixAvarage2(list):
    n = len(list)
    newList = [0]*n
    for i in range(n):
        newList[i] = sum(list[0:i+1]) / (i+1)
    return newList

list2 = [7,6,5,4,3,2,1]
res2 = prefixAvarage2(list2)
print(res2)

# ------------------------------------------------------------
def prefixAvarage3(list):
    n = len(list)
    A = [0]*n
    for i in range(n):
        total += list[i]
        A[i]= total / (i + 1)
    return A
list3 = [7,6,5,4,3,2,1]
res3 = prefixAvarage2(list3)
print(res3)
