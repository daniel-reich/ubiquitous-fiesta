
import re
​
def scrambled(words, mask):
    mask = re.sub('\*', '.', mask) + '$'
    res1 = map(lambda x: re.match(mask, x), words)
    res2 = [x for x in map(lambda m: m.group(0)
                if m != None else None, res1) if x != None]
    return(res2)

