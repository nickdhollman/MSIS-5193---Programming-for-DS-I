# import library\
import re

#read in file
'''
mbox = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 7 - Regex\\mbox.txt')

#print the file
for lines in mbox:
      print(lines)

mbox.close()
'''
mbox = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 7 - Regex\\mbox.txt')

# count the total number of lines (no matter if they have content or not)
# set the counter
count = 0

# loop through the lines in the file
for line in mbox:
    count = count + 1 # counter incremental

# result
print('Line Count:', count)

# close file
mbox.close()

mbox = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 7 - Regex\\mbox.txt')
#### TASK #1 - GET THE TOTAL NUMBER OF LINES WITH CONTENT ####
# set the counter
count = 0

# loop through the lines in the file
#get linecount of mbox
for line in mbox:
      if line != "\n":
            count = count + 1 # counter incremental

# result
print('Line Count:', count)

mbox.close()

### TASK #2 - WRITE A STRING FUNCTION TO GET THE LINES WITH "X-DSPAM-Confidence:” #####

mbox = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 7 - Regex\\mbox.txt')

#define a string function to get the lines with "X-DSPAM-Confidence"
'''
for line in mbox:
    line = line.rstrip()
    if not 'X-DSPAM-Confidence:' in line :
        continue # if not skip the rest of the statements
    print(line)
'''

def function_(line):
    for line in mbox:
        line = line.rstrip()
        if not 'X-DSPAM-Confidence:' in line:
            continue
        print(line)

task2_ = function_(mbox)
print(task2_)

mbox.close()

#### TASK #3 - USE REGEX TO GET ALL THE URLS THAT START WITH "http://" ####
mbox = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 7 - Regex\\mbox.txt')

urllist = list()

for line in mbox:
    line = line.rstrip()
    stuff = re.findall('http://\S+', line) # find the url
    if len(stuff) >=1 : # check if the returned list is not empty
        for i in range(len(stuff)): # go through the returned list
            urllist.append(stuff[i])
print(urllist)

mbox.close()

'''
or line in hand:
    line = line.rstrip()
    stuff = re.findall('[a-zA-Z.]+@[a-zA-Z.]+', line) # find the email address in the line
    if len(stuff) >=1 : # check if the returned list is not empty
        for i in range(len(stuff)): # go through the returned list
            emaillist.append(stuff[i]) # add the emails to the final email list
print(emaillist)
'''