
## Use Bitwise Operator (% modulo operator disallowed.)
def is_odd(n):
    if n & 1 == 1:
        return 'Yes'
    else:
        return 'No'
  
​
## Use Regular Expression (% modulo operator disallowed.)
def is_even(n):
    import re
    if re.match(r"(-?\d*[02468]$)", str(n)):
        return 'Yes'
    else:
        return 'No'

