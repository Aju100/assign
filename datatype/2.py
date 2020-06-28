'''
Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.
'''

input_string = input("Enter string:")
if len(input_string)<2:
    print("")
else:
    print("{}{}".format(input_string[:2],input_string[-2:]))


print(input_string[:-2])