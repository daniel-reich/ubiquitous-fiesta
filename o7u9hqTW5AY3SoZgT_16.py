
import re
​
def switcheroo(txt):
    out = txt
    for sp in [x.span() for x in re.finditer(r'nts\b', txt)]:
        out = out[:sp[0]] + 'nce' + out[sp[1]:]
    for sp in [x.span() for x in re.finditer(r'nce\b', txt)]:
        out = out[:sp[0]] + 'nts' + out[sp[1]:]
    return out

