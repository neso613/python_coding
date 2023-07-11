'''Question: Anagram Check
Write a Python function called is_anagram(str1, str2) that takes two strings as input and returns True if they are anagrams of each other, and False otherwise. Anagrams are words or phrases formed by rearranging the letters of another word or phrase.

For example:
is_anagram("listen", "silent") should return True
is_anagram("hello", "world") should return False
is_anagram("debit card", "bad credit") should return True

You can assume that the input strings will only contain lowercase letters and spaces.# Online Python compiler (interpreter) to run Python online.'''

def is_anagram(str1, str2):
    lis1 = list(str1.lower().replace(' ',''))
    lis2 = list(str2.lower().replace(' ',''))
    for i in lis1:
        if i not in lis2:
            return False
        return True
        
def is_anagram_(str1, str2):
    if sorted(str1.lower()) == sorted(str2.lower()):
        return True
    else:
        return False
    
print(is_anagram("debit card", "bad credit"))       
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
print(is_anagram("hill", "illh"))

print(is_anagram_("debit card", "bad credit"))       
print(is_anagram_("listen", "silent"))
print(is_anagram_("hello", "world"))
print(is_anagram_("hill", "illh"))
