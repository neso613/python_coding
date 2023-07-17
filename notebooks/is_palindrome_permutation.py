'''
Problem: Palindrome Permutation

A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. A permutation is a rearrangement of the characters. Given a string, write a function called is_palindrome_permutation(string) that determines if any permutation of the string can be a palindrome.

For example:

is_palindrome_permutation("aab") should return True because the string "aab" can be rearranged as "aba", which is a palindrome.
is_palindrome_permutation("carerac") should return True because the string "carerac" is already a palindrome.
is_palindrome_permutation("code") should return False because no permutation of the string "code" can form a palindrome.

'''
def is_palindrome_permutation(str1):
    x = sorted(str1.lower().replace(" ",""))
    dictt = {}
    for i in x:
        if i in dictt:
            dictt[i] +=1
        else:
            dictt[i] = 1
    odd_count = 0
    for key,val in dictt.items():
        if val % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
    return True

print(is_palindrome_permutation("aab"))
print(is_palindrome_permutation("carerac"))
print(is_palindrome_permutation("code"))

from collections import Counter
x=Counter("aab")
print(x)



