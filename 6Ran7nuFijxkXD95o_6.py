
import re
def keyboard_shortcut(txt):
    typed = ""
    copied = ""
    txt = re.sub(r'Ctrl \+ C', '&', txt)
    txt = re.sub(r'Ctrl \+ V', '$', txt)
​
    for i in txt:
        if i == "&":
            copied = typed
        elif i == "$":
            typed += copied
        else:
            typed += i
            
    typed = re.sub(r'\s+', ' ', typed)
    return typed.strip()

