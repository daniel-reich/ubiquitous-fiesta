
import re
def change(s):
    s = s.replace('[','').replace(']','')
    return s[1:]*(int(s[0]))
def space_message(txt):
    for i in range(2):
        txt = re.sub(r'\[\w+\]',lambda x:change(x.group(0)),txt)
    return txt

