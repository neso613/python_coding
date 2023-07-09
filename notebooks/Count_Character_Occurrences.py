'''Question: Count Character Occurrences

Write a Python function called count_characters(string) that takes a string as input and returns a dictionary containing the count of each character in the string. The function should ignore whitespace characters and be case-insensitive. The keys of the dictionary should be the characters, and the values should be the counts.

For example, if the input string is "Hello, World!", the function should return the dictionary {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}.'''

def count_characters(s):
    lis = [i for i in s.lower() if i.isalpha()]
    dictt = {}
    for i in lis:
        dictt.__setitem__(i, lis.count(i))
    return dictt

x = count_characters("Hello, World!")
print(x)

x = count_characters("Hey Everyone")
print(x)

