
import re
​
def security(txt):
    txt = txt.strip("$")
    pattern1 = re.compile("Tx*\$")
    pattern2 = re.compile("\$x*T")
    if pattern1.search(txt) or pattern2.search(txt):
        return "ALARM!"
    else:
        return "Safe"

