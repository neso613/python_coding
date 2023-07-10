'''Question: Valid Parentheses

Write a Python function called valid_parentheses(s) that takes a string s containing parentheses (e.g., '(', ')', '{', '}', '[', ']') and returns True if the parentheses are valid and balanced, and False otherwise. Valid parentheses means that each opening parenthesis must have a corresponding closing parenthesis in the correct order.
'''

def valid_parentheses(s):
    mapping = {'(':')','{':'}','[':']'}
    stack = []
    for c in s:
        if c in mapping.keys():
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            elif c in mapping.values():
                ch = stack.pop()
                if mapping[ch]!=c:
                    return False
            else:
                pass
    if len(stack):
        return False
    else:
        return True
print(valid_parentheses('())'))        
print(valid_parentheses('(){}'))
print(valid_parentheses('[{]'))
print(valid_parentheses('{}()[{}]([])'))
