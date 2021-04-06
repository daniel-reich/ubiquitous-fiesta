
from itertools import permutations as perm
​
​
def next_number(num):
    nums = sorted(set(int(''.join(i)) for i in perm(str(num)))) 
    main_num = nums.index(num)
    return num if nums[main_num] == nums[-1] else nums[main_num + 1]

