import re
# List of sentences
Sentences = [
  "aa",
  "ab",
  "abc",
  "abcabcabc",
  "a8qa",
  "abcca"];

print("===== quantifier * ====")
#below syntax will print out any sentences with ab and c repeating 0 or more times, could be ab, abc, abcccc
for s in Sentences:
         if re.search('abc*', s) :
            print(s)
print("=========================")

#below syntax will print out any sentence that has an a and has at least one character before a, could be aa, abcabc, a8qa, abcca
for s in Sentences:
         if re.search('a.*a', s) :
            print(s)
print("=========================")

#below syntax will print out a sentence that contains a or abc
# can be just a such as a8qa, or could be aa, or ab, or abc, or abcca
for s in Sentences:
         if re.search('a(bc)*', s) :
            print(s)
print("=========================")

#below syntax will print out sentences that contain an a, have at least one letter before another a, and end with an a, this is what the a$ syntax states
#examples are aa, a8qa, abcca
for s in Sentences:
         if re.search('a.*a$', s) :
            print(s)

print("===== quantifier + ====")

# + means one or more occurrences, vs * means 0 or more, so abc+ indicates that abc+ has to at least be abc,
# vs abc* could just be ab
for s in Sentences:
         if re.search('abc+', s) :
            print(s)
print("=========================")

# below syntax will print any sentence with a occurring twice, with at least one character between the two as
# in contrast the a.*a could have just been aa with nothing in between 
for s in Sentences:
         if re.search('a.+a', s) :
            print(s)
print("=========================")


#below syntax will print out a sentence that contains abc or abcbc...
#can be abcabcabc or abc or abcca
#in contast a(bc)* could have been aa or ab or abc because bc did not have to occur at least once
for s in Sentences:
         if re.search('a(bc)+', s) :
            print(s)
print("=========================")

# below syntax will print sets that contain a..a and end with an a (because of a$)
for s in Sentences:
         if re.search('a.+a$', s) :
            print(s)

print("===== quantifier ? ====")


# question mark means 0 or 1 occurrences, vs * which means 0 or more occurrences, and $ means 1 or more occurrences
#below syntax will print sentences that have abc or ab
for s in Sentences:
         if re.search('abc?', s) :
            print(s)
print("=========================")


#below syntax will that contain aa or aXa - have 0 or 1 of any character between the a
for s in Sentences:
         if re.search('a.?a', s) :
            print(s)
print("=========================")


#below syntax will contain sentences that contain a or abc
for s in Sentences:
         if re.search('a(bc)?', s) :
            print(s)
print("=========================")


#below syntax will contain sentences that contain aa or aXa AND end with a
for s in Sentences:
         if re.search('a.?a$', s) :
            print(s)

print("===== quantifier {min, max} ====")


#below syntax will print sentences that contain abc or abcc
for s in Sentences:
         if re.search('abc{1,2}', s) :
            print(s)
print("=========================")


#below syntax will print sentences that contain aa or aaa
for s in Sentences:
         if re.search('a{2,}', s) :
            print(s)
print("=========================")


#below syntax will print sentences that contain ab zero times or once
for s in Sentences:
         if re.search('(ab){,1}', s) :
            print(s)
print("=========================")

#below syntax will print sentences that contain  bcc
for s in Sentences:
         if re.search('bc{2}', s) :
            print(s)
