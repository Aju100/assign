hamro_string =  str(input("Enter string: "))

hamro_string = hamro_string.casefold()
reverse_string = reversed(hamro_string)

if list(hamro_string) == list(reverse_string):
    print("Palindrome")
else:
    print("Not Palindrome")
