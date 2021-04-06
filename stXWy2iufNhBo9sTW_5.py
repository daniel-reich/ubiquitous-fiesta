
import re 
def valid_rondo(s):
    if len(s) < 3 or s[0] != "A" or s[len(s)-1] != "A":
        return False 
    if re.findall(r'[A][A-Z][A-Z][A]', s):
        return False 
    return True

