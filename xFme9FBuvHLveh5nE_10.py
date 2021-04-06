
import re
​
​
def is_zygodrome(num):
    return len(re.findall(r"(\d)\1+", str(num))) == len(set(str(num)))

