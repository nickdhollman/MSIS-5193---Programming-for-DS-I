import re
# List of sentences
Sentences = [
  "aa",
  "ab*",
  "abc",
  "abcabcabc",
  "a8qa",
  "abcca"];

print("===== character set ====")
#gets sentences that contain ac or bc
for s in Sentences:
         if re.search('[ab]c', s) :
            print(s)
print("=========================")
#gets sentences that contain one q or p
for s in Sentences:
         if re.search('[qp]+', s) :
            print(s)
print("=========================")
#gets sentences that contain zero or more 1,2,3
for s in Sentences:
         if re.search('[123]*', s) :
            print(s)
print("=========================")
#gets sentences that contain one or more 1,2,3
for s in Sentences:
         if re.search('[1238]+', s) :
            print(s)
print("=========================")
#gets sentences that contain b or * at least once
for s in Sentences:
         if re.search('[b*]+', s) :
            print(s)

# List of sentences
Sentences = [
  "aA",
  "ab*",
  "aBc",
  "XYZ",
  "a8qA",
  "-990"];

print("===== character range ====")
#this syntax will print sentences that contain an uppercase letter
for s in Sentences:
         if re.search('[A-Z]', s) :
            print(s)
print("=========================")
#this syntax will print sentences that contain a digit
for s in Sentences:
         if re.search('[1-9]', s) :
            print(s)
print("=========================")
#this syntax will print sentences that contain a letter or digit
for s in Sentences:
         if re.search('[a-bA-Z1-9]', s) :
            print(s)
print("=========================")
#this syntax will print sentences that contain + or - at least once and a digit
for s in Sentences:
         if re.search('[+\-]+[0-9]', s) :
            print(s)

# List of sentences
Sentences = [
  "aA",
  "ab*",
  "aBc",
  "XYZ",
  "a8qA",
  "cca"];

print("===== negate set ====")
# this syntax will print sentences if it is NOT all uppercase letter
for s in Sentences:
         if re.search('[^A-Z]', s) :
            print(s)
print("=========================")
# this syntax will print sentences if it is NOT all a, c, or B
for s in Sentences:
         if re.search('[^acB]', s) :
            print(s)

# class ex
# given the following
Sentences = ["aA","ab*","aBc","abcabcabc","a8qA","-990"];

print("==============class exercise============")
#print sentences that start with "a" and end with "c"
for s in Sentences:
         if re.search('^a.+c$', s) :
            print(s)