
import re
​
def num_in_str(lst):
    return [i for i in lst if len(re.findall("\d", i)) > 0]

