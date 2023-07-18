'''
Problem: Missing Number

You are given an array of unique integers from 0 to n, with one element missing. Write a function called find_missing_number(nums) that finds and returns the missing number.

For example:

find_missing_number([3, 0, 1]) should return 2 because the missing number is 2.
find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) should return 8 because the missing number is 8.
'''

def find_missing_number(numbers_list):
    n = len(numbers_list)
    expected_sum = int((n * (n + 1)) / 2)
    actual_sum = sum(numbers_list)
    missing_num = expected_sum - actual_sum
    return missing_num
    
print(find_missing_number([3, 0, 1]))
print(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
