# initialize a String variable s
s = 'Hello, OSU friends!'
# get the length of the string s
slength = len(s)
print(slength)

# get the "Hello" from the string s - below code will get 0 - 4 character, not 5
shello = s[0:5]
print(shello)

# check if OSU is in the string s
if ('OSU' in s):
    print("Yes!")
else:
    print("No!")

# check if OK is in the string s
if ('OK' in s):
    print("Yes!")
else:
    print("No!")

# print out the last character in string s
print(s[-1])

#in class exercise #
#assign string "Python is a useful scripting language" to variable p
p = 'Python is a useful scripting language'
print(p)
#get the word useful from string p
useful = p[12:18]
print(useful)
#check the length of p
plength = len(p)
print(plength)