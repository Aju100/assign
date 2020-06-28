'''
Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
'''

def lol(str1):

    char = str1[0]
    str1 = str1.replace(char,'$')
    str1 = char+str1[1:]

    return str1
str2 = input("enter string:")

print(lol(str2))
