
import re
​
def count_smileys(lst):
    return len(re.findall(r'[:;][-~]?[)D]', ''.join(lst)))

