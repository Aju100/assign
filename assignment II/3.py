def getAnagramFromParagraph(input_string):
    word_list = input_string.split()
    anagram_list = []
# o(n*2)
    for word in word_list:
        for each in word_list:
            if sorted(word) == sorted(each) and word != each:
                anagram_list.append(word)
    return sorted(set(anagram_list))

input_data = str(input("Enter string:"))
print(getAnagramFromParagraph(input_data))