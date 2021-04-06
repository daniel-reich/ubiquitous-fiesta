
from collections import Counter
def single_number(nums):
    for k, v in Counter(nums).items():
        if v == 1:
            return k

