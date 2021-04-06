
import re
def decrypt(s):
    return re.sub(r'\d{2}#|\d',lambda x: chr(96 + int(x.group(0)[:2])) if '#' in x.group(0) else chr(96 + int(x.group(0)[0])),s)

