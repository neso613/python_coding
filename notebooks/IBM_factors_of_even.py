def even(start,n):
    start = start + 1 if start % 2 else start
    return list(range(start,start+n*2,2))
    
print(even(2,4))
print(even(1,3))
print(even(5,6))
