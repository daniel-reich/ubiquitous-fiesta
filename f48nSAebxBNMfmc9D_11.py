
import re
​
def scrambled(words, mask):
    pattern = re.compile("^"+mask.replace("*",".")+"$")
    return [i for i in words if pattern.match(i)]

