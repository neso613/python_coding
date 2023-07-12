'''
You are given a sentence, and want to shift each letter by 2 in alphabet to create a secret code. The sentence you want to encode is 'the lazy dog jumped over the quick brown fox' and the output should be ’vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz’
'''

import string

in_str = 'the lazy dog jumped over the quick brown fox'
out_str = []
dict_char = {}
dict_num = {}

for i,letter in enumerate(string.ascii_lowercase):
    dict_char.__setitem__(letter,i)
    dict_num.__setitem__(i,letter)

for i in in_str:
    if i.isalpha():
        val = dict_char[i]
        if val == 25:
            incremented_val = 1
        elif val == 24:
            incremented_val = 0
        else:
            incremented_val = val + 2
        new_char = dict_num[incremented_val]
        out_str.append(new_char)
    else:
        out_str.append(i)  
new_str = ''.join(out_str)       
print(new_str)
