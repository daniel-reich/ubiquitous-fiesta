
import re
​
## Use Bitwise Operator (% modulo operator disallowed.)
def is_odd(n):
    return "Yes" if (n & 1) else "No"
​
## Use Regular Expression (% modulo operator disallowed.)
def is_even(n):
    return "Yes" if re.findall(r'\d*[02468]$', n) else "No"

