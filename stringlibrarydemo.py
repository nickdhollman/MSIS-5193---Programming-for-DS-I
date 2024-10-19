import re

stuff = 'Hello world'
print(type(stuff)) # show string type
print(dir(stuff))  # list all function in the string library

greet = 'Hello Bob'

# upper case all characters
nnn = greet.upper()
print(nnn)

# upper case all characters
www = greet.lower()
print(www)

# replace Bob with Jane
nstr = greet.replace('Bob','Jane')
print(nstr) #Hello Jane

# replace o with X
nstr = greet.replace('o','X')
print(nstr) #HellX BXb

greet = '   Hello Bob  '

# strip the left side spaces
lstrip = greet.lstrip() #'Hello Bob  '
print(lstrip)

# strip the right side spaces
rstrip = greet.rstrip() #'   Hello Bob'
print(rstrip)

# strip both side spaces
bstrip = greet.strip() #'Hello Bob'
print(bstrip)

line = 'Hello Bob'
# split into a list of words using space
words = line.split(' ') # ['Hello', 'Bob']
print(words)
#return value will be an array of words

line = 'Hello, Bob'
# split into a list of words using comma
words = line.split(',') # ['Hello', ' Bob']
print(words)

# split into a list of words using space or comma - this is accounting for the space after the comma in the previous example so the output
# does not have a space before Bob
words = re.split(", | ",line) # ['Hello', 'Bob']
print(words)

s = 'abracadabra'
print(s.index('a')) # 0 - index location of a
print(s.index('rac')) # 2 - this is the location where the position STARTS for 'rac'
print(s.count('a')) # 5 - this will return the # of times 'a' occurs in the string defined
print(s.count('b')) # 2
print(s.count('x')) # 0 - x does not occur so a value of 0 is returned

# class exercise - given a string 'W3Resource' generate 'w3ce'
r = 'W3Resource'
rlower = r.lower()
print(rlower)
r_rep = rlower.replace("resour","")
print(r_rep)

