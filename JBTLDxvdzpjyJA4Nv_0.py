
import re
​
def super_reduced_string(txt):
    while re.search(r'(.)\1', txt):
        txt = re.sub(r'(.)\1', '', txt)
    return txt if txt else 'Empty String'

