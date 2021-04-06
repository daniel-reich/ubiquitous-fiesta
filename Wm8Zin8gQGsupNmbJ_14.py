
import re
def binary_conversion(txt):
    r = r'(\d{8})'
    m = re.findall(r, txt)
    
    t= len(m)
    s = ''
    for i in range(t):
        s = s + chr(int(m[i], 2))
    return s

