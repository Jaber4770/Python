str1 = 'Hello world!'
print(str1[4])

length = len(str1)
print(length)

print(str1[len(str1)-1])

# printing letter from the string
string1 = "I wandered lonely as a cloud..."
i = 0
while i <len(string1):
    letter = string1[i]
    print(letter)
    i +=1
    
# using for loop
for letter in string1:
    print("From for loop: ",letter)
    
# slice
stringx = 'the quick brown fox jumps over the lazy dog.'
print(stringx[0:4])

# print(stringx[:7]) return from 0-6
# print(stringx[7:7]) return empty
# print(stringx[2:]) return from 2 index to last of the string
# print(stringx[4:1]) return empty
# print(stringx[:]) return full string

# id return the memoryy address, wheere the element are located
stringId = id(stringx)
print(stringId)


# finding index of a letter
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find("Hello", 'l'))

# counting letter
def countLeter(text,letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    return count

count = countLeter("the quick brown fox jumps over the lazy dog", 't')
print("the letteer is available: ",count, "timees")


capitalText = stringx.capitalize()
print(capitalText)

print(stringx.center(40, '-'))
print(stringx.count('e'))


stringb = "Hello"
print(stringb.center(40, '-'))


file = 'goofy.exe'
print(file.endswith("exe"))

print(file.find('fy'))
print(file.ljust(40))
print(file.rjust(50))
print(file.replace('g','G'))

print('y' in file)
print('t' in file)

for letter in file:
    print(letter)

def in_both(word1,worrd2):
    for letter in word1:
        if letter in worrd2:
            print(letter)

in_both('hello', 'the quick brown fox.')

aaa = 'ciao'
bbb = 'CIAO'
print(aaa==bbb)
print(aaa>bbb)
print(aaa<bbb)
bbb="Ciao"
print(aaa>bbb)


""" Write a program that reads a number between 1,000 and 999,999
from the user and prints it with a comma separating the thousands. """
def formating(number):
    number = int(number)
    if(number>1000 and number < 999999):
        formatted = '{:,}'.format(number)
        print("formated number is: ",formatted)
    else:
        print('Number is out of range.')

print('write a number between 1000 and 999,999')
formating( input())










