
import re
​
def tweet(txt):
    x = re.findall("[@,#]\w+",txt)
    usrhndl = ''
    for items in x:
        usrhndl += items+' '
​
    return usrhndl[:-1]

