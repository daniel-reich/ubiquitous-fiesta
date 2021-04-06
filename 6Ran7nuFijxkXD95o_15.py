
import re
def keyboard_shortcut(txt):
    clip = ''
    while True:
        m = re.search(r'Ctrl \+ C\s?|Ctrl \+ V\s?', txt)
        if not m: break
        if '+ C' in m.group(0):
            clip = txt[:m.start()]
            txt = txt.replace(m.group(0), '', 1)
        else:
            txt = txt.replace(m.group(0), clip, 1)
    return txt.rstrip()

