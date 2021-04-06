
import re
​
def letters_only(s):
    return bool(re.match('[a-z ]+$', s))

