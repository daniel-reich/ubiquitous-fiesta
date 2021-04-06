
import re
def direction(lst):
    return list(map(lambda x:re.sub('A','E',re.sub(r'a','e',re.sub(r'E','W',re.sub(r'e','w',x)))), lst))

