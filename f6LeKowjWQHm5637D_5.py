
import re
​
def cap_to_front(s):
    capitals = re.findall(r'[A-Z]+', s)
    lowers = re.findall(r'[a-z]+', s)
    return ''.join(capitals + lowers)

