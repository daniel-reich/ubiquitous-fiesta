
import re
​
def replace(txt, r):
    return re.sub('['+r[0]+'-'+r[-1]+']', '#', txt)

