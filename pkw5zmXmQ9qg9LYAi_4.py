
import re
def space_message(txt):
    while re.match(r".*\[", txt):
        txt = re.sub(r"\[(\d+)(\w+)\]", lambda x: int(x.group(1))*x.group(2), txt)
    return txt

