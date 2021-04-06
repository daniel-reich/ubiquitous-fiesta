
from re import match
is_odd = lambda n: "Yes" if n & 1 else "No"
is_even = lambda n: "Yes" if match(".*[02468]$", n) else "No"

