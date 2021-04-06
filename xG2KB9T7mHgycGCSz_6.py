
import re
​
def valid(pin):
    return bool(re.match('^\d{4}$|^\d{6}$', pin))

