
import re
​
​
def censor_string(txt, lst, char):
    new_txt = txt
    for word in lst:
        new_txt = re.sub(r"\b{}(?=\b|$)".format(word), char*len(word), new_txt)
    return new_txt

