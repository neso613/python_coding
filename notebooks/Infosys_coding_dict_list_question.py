# count the number of times each character occurs in the list
lis = ["am", "typing", "new", "rohit", "code", "continue", "continues", "new_string", "I"]

# Create a dictionary with keys from 'a' to 'z' and initial values
dictt = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

# Print the dictionary
print(dictt)

for word in lis:
  for char in word:
      if char.isalpha():
          char = char.lower()
          dictt[char] += 1
print(dictt)
