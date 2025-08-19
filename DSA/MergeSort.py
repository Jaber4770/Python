def merge(s1,s2,s):
    i = j = 0
    while i+j < len(s):
        if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
            print("IF: ", i, '\t', j, '\t')
            s[i+j] = s1[i]
            i += 1
        else:
            print("ELSE: ", i, '\t', j, '\t')
            s[i+j] = s2[j]
            j += 1