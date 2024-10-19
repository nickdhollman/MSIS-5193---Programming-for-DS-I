# by default if we don't specify the read mode in the below open function, it will use the 'r' option which is read mode, if we want to write we would need to use 'w' function
xfile = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\mbox-short.txt')
print(xfile)

#the new line character itself is a character, so will be included in the length calculation
# read lines from the text file, and show the length of each line
for cheese in xfile:
      print(cheese)
      print(len(cheese)) # the length includes the new line character

xfile.close()

xfile = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\mbox-short.txt')
# read lines from the text file, and show the length of each line
# without including the new line character
for cheese in xfile:
      sentence = cheese.strip("\n") # remove the new line character at the end
      print(sentence)
      print(len(sentence))

xfile.close()

class_ = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\clown.txt')
print(class_)
# read lines from the text file, and show the length of each line
for cheese in class_:
      print(cheese)
      print(len(cheese)) # the length includes the new line character

class_.close()

#in class exercise - read clown.txt, then remove all the 'the' in the file
class_ = open('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 6 - String and Text File\\clown.txt')
for cheese in class_:
      no_the = cheese.replace(" the","") # remove the 'the' from the output
      print(no_the)
      print(len(no_the))

class_.close()
