'''Question: Subarray with Target Sum

Write a Python function called subarray_with_target_sum(nums, target) that takes a list of integers nums and a target integer target as input. The function should find and return the subarray (contiguous elements) in nums that sums up to the target. If no such subarray exists, the function should return an empty list.

For example:

subarray_with_target_sum([1, 2, 3, 4, 5], 9) should return [2, 3, 4]
subarray_with_target_sum([4, 6, 7, 8, 10], 23) should return [6, 7, 10]
subarray_with_target_sum([2, 4, 6, 8, 10], 7) should return [] (no subarray sums up to 7)
'''
lis,target = [1, 2, 3, 4, 5],9
stack = []
for i in range(len(lis)):
    stack.append(lis[i])
    stack_sum = sum(stack)
    if stack_sum == target:
        break
    elif stack_sum > target:
        num = stack.pop(0)
        stack_sum = stack_sum - num
        if stack_sum == target:
            break
print(stack)





















