
import re
​
def scrambled(words, mask):
    regex = re.compile(mask.replace('*', '.') + '$')
    return [i for i in words if regex.match(i)]

