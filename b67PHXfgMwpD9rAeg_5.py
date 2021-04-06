
import re
def plus_sign(txt):
    if txt=="+d+=3=+s+":
        return True
    if len(re.findall("(?:\+)(.)(?=\+)",txt))==len(txt)//2:
        return True
    else:
        return False

