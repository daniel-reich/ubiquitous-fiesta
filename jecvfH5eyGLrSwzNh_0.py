
import re
​
def fauna_number(txt):
    animals = ["muggercrocodile","one-hornedrhino","python","moth","monitorlizard","bengaltiger"]
    return [(j, i) for i, j in re.findall('(\d+) ([a-z-]+)', txt) if j in animals]

