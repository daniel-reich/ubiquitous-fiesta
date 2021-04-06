
import re 
def letters_only(s):
    return bool(re.findall('^[a-z\s]+$',s))

