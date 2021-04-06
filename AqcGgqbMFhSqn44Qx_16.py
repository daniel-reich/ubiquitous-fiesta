
import re
def tweet(txt):
    return " ".join(x for x in re.findall("@\\w+|#\\w+", txt))

