
import re
​
def replace_nums(s):
    return re.sub(r'\d+', lambda x: bin(int(x.group()))[2:], s)

