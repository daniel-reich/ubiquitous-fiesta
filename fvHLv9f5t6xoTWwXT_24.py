
import re
​
​
def grab_number_sum(s):
    nums = re.findall(r'\d+', s)
    return sum(int(n) for n in nums)

