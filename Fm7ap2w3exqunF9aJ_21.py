
import re
def count_lone_ones(n):
    num=str(n)
    pattern = re.compile(r'(1){2,20}')
    matches = pattern.finditer(num)
    k = "".join(i.group(0) for i in matches)
    return num.count("1")-len(k)

