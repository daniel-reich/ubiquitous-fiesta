
import re
def is_palindrome(txt):
    txt = re.sub(r'[^\w\s]','',txt)
    txt = txt.replace(' ','').lower()
    return txt==txt[::-1]

