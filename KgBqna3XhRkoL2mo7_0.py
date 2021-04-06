
import re
​
def decrypt(s):
    return ''.join(chr(int(i) + 96) for i in re.findall(r'\d{2}(?=#)|\d', s))

