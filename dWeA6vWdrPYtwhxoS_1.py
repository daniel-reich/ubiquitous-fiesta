
import re
def count_number(lst):
    return len(re.findall(r'-?\d+.?\d*', str(lst)))

