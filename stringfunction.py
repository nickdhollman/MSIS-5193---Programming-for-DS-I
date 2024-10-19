
# when defining functions, after def (function name(function object)):, you will need to indent for the remainder of the function, then unindent when you are done with the function
# and want to resume other code
def middle(text):
#Returns: middle 3rd of text  Param text: a string
    # Get length of text
    size = len(text)
    # Start of middle third - '//' is float division, this will divide a number by 3 and then get the result to the nearest whole number
    start = size//3
    # End of middle third - this end value is actually the start of the last third, but will not be included because in [start:end] end will not be included in the sliced value output
    end = 2*size//3
    # Get the text - this must be a slice of the text
    result = text[start:end]
    # Return the result
    return result

def firstparens(text):
#Returns: substring in () , Uses the first set of parens  Param text: a  string with ()
    # Find the open parenthesis
    start = text.index('(')
    # Store string  AFTER parenthesis to tail - this will store everything after the first '(' and store it in a new variable labeled 'tail'
    tail = text[start+1:]
    # Find the close parenthesis
    end = tail.index(')')
    # Return the result - this will take the variable tail that has everything after the first '(' and keep everything until the close parentheses ')'
    return tail[:end]


s = 'aabbcc'
print(middle(s))

s = 'Hello, Welcome to OSU (Spears) School of Business (Stillwater)!'
print(firstparens(s))

#in class exercise - define function to get a string made of the first three characters
#of a specified string. If the length of the string is less than 3, return the original string

#sample function and results
#first_three('ipy' -> ipy
#first_three('python' -> pyt

def first_three(text):
    if len(text) < 3:
        return text[0:]
    if len(text) >= 3:
        return text[0:3]

test1 = first_three('ipy')
print(test1)
test2 = first_three('python')
print(test2)