
import re
​
def increment_string(txt):
    if txt[-1] not in '0123456789':
        return txt + '1'
    txt, num = re.findall(r'\D+|\d+', txt)
    txt += str(int(num) + 1).zfill(len(num))
    return txt

