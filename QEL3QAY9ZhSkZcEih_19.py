
import re
​
​
def is_odd(n):
    return 'Yes' if bin(abs(n))[-1] == '1' else 'No'
​
​
def is_even(n):
    return 'Yes' if bool(re.match(r'[-\d]*[02468]$', n)) else 'No'

