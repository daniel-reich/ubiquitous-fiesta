
import re
def switcheroo(txt):
    return re.sub(r'(nts|nce)\b',lambda x:'nce' if x.group(0)=='nts' else 'nts',txt)

