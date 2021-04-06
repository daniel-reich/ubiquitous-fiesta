
import re
​
def space_message(txt):
    while '[' in txt:
        txt = re.sub(r'\[([0-9])([A-Z]+)\]', lambda x: x.group(2)*int(x.group(1)), txt)
    return txt

