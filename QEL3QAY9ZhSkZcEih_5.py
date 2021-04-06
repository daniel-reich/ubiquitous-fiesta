
## Use Bitwise Operator (% modulo operator disallowed.)
is_odd=lambda n:"Yes"if abs(n)>>1!=abs(n)/2else"No"
## Use Regular Expression (% modulo operator disallowed.)
import re
is_even=lambda n:"Yes"if re.fullmatch("-?\d*[02468]",n)else"No"

