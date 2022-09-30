"""
Python interview question

Sort 0's and 1's left to right
0's on the left and 1's on the right

- Time complexity O(n)
- Space complexity O(1) - It should be in place, cannot create a new array
- Cannot use the length function
"""

lst = [0,1,1,1,0,0,1,0,1]

try:
    i, j = 0, 1
    while(1):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        elif lst[i] < lst[j]:
            i += 1
        j += 1
except IndexError:
    print(lst)
