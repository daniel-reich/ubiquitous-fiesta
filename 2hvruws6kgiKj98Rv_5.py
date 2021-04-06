
import re
​
def to_scottish_screaming(txt):
​
    return ''.join(re.sub(r'[aiou]','e',txt.lower())).upper()

