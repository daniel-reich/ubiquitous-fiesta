
import re
def next_letters(s):
    a, b, c = re.match(r'^(\w*?)([^Z]?)(Z*)$', s).groups()
    return a + (chr(ord(b)+1) if b else 'A') + 'A'*len(c)

