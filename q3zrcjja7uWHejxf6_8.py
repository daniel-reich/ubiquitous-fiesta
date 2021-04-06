
import re
​
def negative_sum(chars):
    return sum(int(i) for i in re.findall('-\d+', chars))

