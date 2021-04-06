
from collections import Counter
def single_number(nums):
    cnt = Counter(nums)
    for num in cnt:
        if cnt[num] == 1:
            return num

