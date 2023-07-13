'''
Write a Python function called reverse_vowels(string) that takes a string as input and returns a new string with the vowels reversed. In the reversed string, only the vowels (a, e, i, o, u) should be reversed while maintaining the order of the consonants and other characters. You can assume that the input string will only contain lowercase letters.
For example:

reverse_vowels("hello") should return "holle"
reverse_vowels("python") should return "python"
reverse_vowels("programming") should return "prigrammong"
'''
str1 = 'programming'
str1 = str1.lower()
vowel_count = 0
stack = []
vowel = ['a','e','i','o','u']

for i, char in enumerate(str1):
    if char in vowel:
        stack.append(char)
        str1 = str1[:i] + '_' + str1[i+1:]
        vowel_count += 1
for i, char in enumerate(str1):
    if char == '_':
        if vowel_count > 0:
            str1 = str1[:i] + stack.pop() + str1[i+1:]
            vowel_count -= 1
        else:
            break
print(str1)
