
from collections import Counter
​
def single_number(nums):
    C = Counter(nums)
    return [k for k,v in C.items() if v == 1][0]

