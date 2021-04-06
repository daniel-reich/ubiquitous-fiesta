
import re
strip = re.compile(r'\D')
​
​
def text_to_number_binary(txt):
    txt = txt.lower().replace('one', '1')
    txt = txt.replace('zero', '0')
    txt = strip.sub('', txt)
    while len(txt) % 8 != 0:
        txt = txt[:-1]
    return txt

