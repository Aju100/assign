'''
Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
'''

input_string  = input("Enter string:")
length = len(input_string)

if length >=3:
    if input_string[-3:] == 'ing':
        print(input_string+'ly')
    else:
        print(input_string+'ing')