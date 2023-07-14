'''
Question: Merge Intervals

Write a Python function called merge_intervals(intervals) that takes a list of intervals as input and returns a new list of merged intervals. Each interval in the input list is represented as a pair of integers [start, end], where start represents the starting point of the interval and end represents the ending point of the interval. The intervals in the input list may overlap or be disjointed.

Your task is to merge overlapping intervals and return a new list of non-overlapping intervals.

For example:

merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) should return [[1, 6], [8, 10], [15, 18]]
merge_intervals([[1, 4], [4, 5]]) should return [[1, 5]]
merge_intervals([[1, 7], [3, 9], [8, 10]]) should return [[1, 10]]
'''
def merge_intervals(in_data):
    n = len(in_data)
    stack = []
    in_data.sort(key=lambda x : x[0])
    stack.append(in_data[0])
    for start,end in in_data[1:]:
        lastEnd = stack[-1][1] 
        if start<= lastEnd:  # overlapping 
            stack[-1][1] = max(lastEnd,end)
        else:
            stack.append([start,end])
    return stack

print(merge_intervals([[2, 6], [8, 10], [1, 3],[15, 18]]))
print(merge_intervals([[1, 4], [4, 5]]))
print(merge_intervals([[2, 6], [3, 8]]))
print(merge_intervals([[1, 7], [8, 10], [3, 9]]))













