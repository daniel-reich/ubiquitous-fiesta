
import re
def camelCasing(txt):
    t = re.compile("[^A-Za-z]+")
    w = t.split(txt)
    return ''.join(w1.lower() if i is 0 else w1.title() for i, w1 in enumerate(w))

