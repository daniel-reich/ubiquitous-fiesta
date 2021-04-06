
import re
​
def count_lone_ones(n):
    return 0 if "1" not in str(n) else sum(1 if len(one) == 1 else 0 for one in re.findall(r"1+", str(n)))

