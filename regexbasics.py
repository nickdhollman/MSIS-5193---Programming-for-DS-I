# Regular expression library
import re

# Add or remove the words in this list to vary the results
wordlist = ["color", "colour", "work", "working", "fox", "worker", "working"]

#below syntax is printing any words with 'or' with at least one letter before 'or'
for word in wordlist:
         if re.search('.or', word) :
            print (word)


# List of sentences
Sentences = [
  "The sun is shining",
  "Apples are delicious",
  "The moon is bright",
  "Birds are singing"];

#below syntax will print out any sentences that start with 'The'
for s in Sentences:
         if re.search('^The', s) :
            print(s)
#below syntax will print out any sentences that end with 'ing'
for s in Sentences:
         if re.search('ing$', s) :
            print(s)

# '|' specifies an OR logic operator, there is no AND operator in regular expression

# List of sentences
Sentences = [
  "Subject: abc is here!",
  "Date: 2023-09-05",
  "The Subject to discuss...",
  "Action from Date ..."];

#below syntax will print any sentences that start with 'Subject' or contain 'Date' in the sentence
for s in Sentences:
         if re.search('^Subject|Date', s) :
            print(s)
print("===============")

#below syntax will print any sentences that start with 'Subject' or start with 'Date'
#notice how this code compared to the above does not print 'Action from Date' because it only prints sentences that start with date
for s in Sentences: # get sentences end with “ing”
         if re.search('^(Subject|Date)', s) :
            print(s)

# List of sentences
Sentences = [
  "Subject: abc is here!",
  "Date: 2023-09-05",
  "The Subject to discuss...",
  "Action from Date to..."];

for s in Sentences: # get sentences contain 'Subject to' or 'Date to'
         if re.search('(Subject|Date) to', s) :
            print(s)

# List of sentences
Sentences = [
  "Subject: abc is here!",
  "Date: 2023-09-05",
  "The Subject to discuss...?",
  "Action from Date to..."];

for s in Sentences: # get sentences contain '!' or '?'
         if re.search('!|\\?', s) :
            print(s)

# in class ex
Sentences = [
  "Subject: abc is here!",
  "Date: 2023-09-05?",
  "The Subject to discuss is...?",
  "Action from Date to..."];

#script to find sentences that has is or ?
# output should print all except Action from Date to...
for s in Sentences:
         if re.search('is|\\?', s) :
            print(s)



