'''Question: Group Anagrams

Given a list of strings, write a function called group_anagrams(strs) that groups the anagrams together and returns them as a list of lists. An anagram is a word formed by rearranging the letters of another word.

For example:

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) should return [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]].
group_anagrams(["listen", "silent", "rest", "best", "erst"]) should return [["listen", "silent"], ["rest", "erst"], ["best"]].
'''
stack = {}
anagram_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

for i in anagram_list:
    sorted_word = ''.join(sorted(i))
    if sorted_word not in stack:
        stack[sorted_word]= [i]
    else:
        stack[sorted_word].append(i)
print(stack.values())






































