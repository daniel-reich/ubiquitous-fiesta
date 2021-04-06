
import re
​
def is_authentic_skewer(s):
    if '-' not in s or set(s) == {'-'}:
        return False
    gap = re.split('\w', s)[1]
    return bool(re.match('([^AEIOU]{0}[AEIOU]{0})+[^AEIOU]\Z'.format(gap), s))

