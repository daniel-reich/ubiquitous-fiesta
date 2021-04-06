
import re
def is_odd(n):
    return 'Yes' if n&1 else 'No'
  
def is_even(n):
    return 'Yes' if re.findall(r'[24680]$', n) else 'No'

