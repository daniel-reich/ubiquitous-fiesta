
from collections import namedtuple
​
MaxArray = namedtuple("MaxArray", "array size")
​
​
def is_odd_subarray(arr, size):
    for row in range(size):
        for col in range(size):
            if arr[row][col] % 2 == 0:
                return False
    return True
​
​
def get_sub(arr, r, c, size):
    sub = [[0] * size for x in range(size)]
    for row in range(size):
        for col in range(size):
            sub[row][col] = arr[row + r][col + c]
    return sub
​
​
def odd_square_patch(arr):
    max_sized = MaxArray(None, 0)
    size_row, size_col = len(arr), len(arr[0])
    size = min(size_col, size_row)
    sub = []
    for r in range(size_row):
        for c in range(size_col):
            for s in range(1, size + 1):
                if (c + s) <= size_col and (r + s) <= size_row:
                    sub = get_sub(arr, r, c, s)
                    if not is_odd_subarray(sub, s):
                        break
                    elif max_sized.size < s:
                        max_sized = MaxArray(sub, s)
    return max_sized.size

