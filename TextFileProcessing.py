fhand = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\mbox-short.txt')

# set the counter
count = 0

# loop through the lines in the file
for line in fhand:
    count = count + 1 # counter incremental

# result
print('Line Count:', count)

# close file
fhand.close()

# read whole as a string
fhand = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\mbox-short.txt')
wholefile = fhand.read()

# get the total characters in the file
print(len(wholefile))

# get the first 20 character
print(wholefile[:20])

# close file
fhand.close()

fhand = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\mbox-short.txt')

# search for lines start with 'From:'
for line in fhand:
    if line.startswith('From:'):
        print(line)

# close file
fhand.close()

fhand = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\mbox-short.txt')

# search for lines start with 'From:'
for line in fhand:
    if line.startswith('From:'):
        newline = line.rstrip() # remove the whitespace and new line from the end
        print(newline)

# close file
fhand.close()

fhand = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') : # check if it start with 'From:'
        continue # if not skip the rest of the statements - this saves processing time, if the line does not start with 'From:' we are going to skip the remainder of the loop
        # and go back to the beginning of the next line - so it will skip the print line
    print(line)

# close file
fhand.close()

fhand = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if not 'uct.ac.za' in line : # check if domain 'uct.ac.za' is in the line
        continue # if not skip the rest of the statements
    print(line)

# close file
fhand.close()

# in class exercise - use words.txt file and count the number of words that contain 'un'
class_ = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\words.txt')

# set the counter
count = 0

# loop through the lines in the file
for line in class_:
    count = count + 1 # counter incremental

# result
print('Line Count:', count)

# close file
class_.close()

class_ = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\words.txt')

#set the counter
count = 0

#what are we wanting to count
un = 'un'

# loop through the lines in the file to count un
for line in class_:
    if un in line:
        count = count + 1 # counter incremental

print('un count', count)

#close the file
class_.close()