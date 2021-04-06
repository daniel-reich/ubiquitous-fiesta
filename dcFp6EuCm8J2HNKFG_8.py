
import re
def func(lst):
    return sum(len(lst[i]) for i in range(len(lst)) if re.search('\w+',str(lst[i])))+str(lst).count('[')-1

