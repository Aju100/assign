#Write a Python program to count the number of characters (character frequency) in a string.

input_string = input("Enter an string:")
input_string = input_string.lower()
dict ={}

for _ in input_string:
    dict[_] = dict.get(_,0)+1

print(str(dict))
