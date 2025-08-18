# dictionary
thisdict = {
    "band":"ford",
    "model": "mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["band"])

# lenght len
print(len(thisdict))

print("band" in thisdict)


myKeys = thisdict.keys()
print(myKeys)
myValues = thisdict.values()
print(myValues)


""" Count how many times each letter is contained in a given
string """

text = "banana"
letter_counts = {}

for char in text:
    if(char.isalpha()):
        char = char.lower()
        letter_counts[char]= letter_counts.get(char, 0)+1
        
print(letter_counts)



""" – Count how many times each letter is contained in a given
string
– Create a list containing 26 elements initially set to zero, each
corresponding to a different letter of the alphabet. Traverse
the string and increment the list element corresponding to the
current letter. (lousy) """

textt = 'helloworld'
counts = [0] * 26
for char in textt:
    if char.isalpha():
        index = ord(char)-ord('a')
        counts[index] +=1
for i in range(26):
    if counts[i]>0:
        letter = chr(i+ord('a'))
        print(letter, ":", counts[i])
        










