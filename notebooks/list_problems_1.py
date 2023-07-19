'''
Problem: Two Sum

Given an array of integers and a target integer, write a function called two_sum(nums, target) that finds and returns the indices of two elements in the array such that they add up to the target.

Assume that there is exactly one solution, and you cannot use the same element twice.

For example:

two_sum([2, 7, 11, 15], 9) should return [0, 1] because nums[0] + nums[1] = 2 + 7 = 9.
two_sum([3, 2, 4], 6) should return [1, 2] because nums[1] + nums[2] = 2 + 4 = 6.
'''
def two_sum(numbers,target):
    index = {}
    for number in numbers:
        should_be_num = target-number
        if should_be_num in index:
            return [index[should_be_num],numbers.index(number)]
        index.__setitem__(number,numbers.index(number))
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))


