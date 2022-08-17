# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


def alphabetize(string):
    string = list(string)
    string.sort()
    return "".join(string)

alphabetized_string= input('Give me a string to alphabetize  ')

print(alphabetize(alphabetized_string))


