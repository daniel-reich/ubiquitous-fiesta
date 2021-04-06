
import re
​
​
def count_smileys(array):
    pattern = r'[:;]+[-~]?[\)D]+'
    txt = ' '.join(array)
    return len(re.findall(pattern, txt))

