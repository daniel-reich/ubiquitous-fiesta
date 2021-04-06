
import re
​
def ing_extractor(s):
    return [i for i in s.split() if re.search('[aeiou\W][^aeiou]{1,3}ing$', i, re.I)]

