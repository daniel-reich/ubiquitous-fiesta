
import re
def deep_sum(lst):
    return sum(map(int, re.findall(r"-?\d+", str(lst))))

