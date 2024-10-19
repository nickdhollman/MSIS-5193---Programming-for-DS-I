import re

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x) # find all numbers and return a list
print(y)

y = re.findall('[A-Z]\S+',x) # find words contain an uppercase letter followed by a non-whitespace character
print(y)

y = re.findall('[ABC]',x) # find all words that contain uppercase characters 'A' 'B' or 'C'
print(y)

y = re.findall('[MABC]',x) # find all words that contain uppercase characters 'A' 'B' or 'C'
print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

y = re.findall('\S+@\S+',x) # find the email address - asking for any words with at least one non-whitspace character before and after '@'
print(y)

y = re.findall('@([^ ]*)',x) # get the email domain - this is asking for the text after the @ that is non-whitespace
print(y)


########## process file ####################

hand = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\mbox-short.txt') # read a file

emaillist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('[a-zA-Z.]+@[a-zA-Z.]+', line) # find the email address in the line
    if len(stuff) >=1 : # check if the returned list is not empty
        for i in range(len(stuff)): # go through the returned list
            emaillist.append(stuff[i]) # add the emails to the final email list
print(emaillist)

#class ex - find all the IP addresses for the mbox text file
hand = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\mbox-short.txt') # read a f
IPADD = list()

for line in hand:
    line = line.rstrip()
    stuff_IP = re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", line) # find the email address in the line
    # [0-9] indicates that wer are looking for any of the integer values 0 - 9 inside of brackets
    # {1,3} indicates that we are looking for as few as one or as many of three digits
    #\. because . is a special character, so we have to use \ before the . to find the actual character
    if len(stuff_IP) >=1 : # check if the returned list is not empty
        for i in range(len(stuff_IP)): # go through the returned list
            IPADD.append(stuff_IP[i]) # add the emails to the final email list
print(IPADD)

hand.close()