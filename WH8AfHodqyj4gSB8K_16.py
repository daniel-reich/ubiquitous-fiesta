
import re
def is_authentic_skewer(s):
    rex = r'[^{0}(\-*)[{0}\1[^{0}(\1[{0}\1[^{0})*$'.format(r'AEIOU\-]')
    return bool(re.match(rex, s))

