
def is_odd(n):
    return 'Yes' if n&1 else 'No'
import re
def is_even(n):
    return 'Yes' if len(re.findall(r'[02468]$',str(n)))!=0 else 'No'

