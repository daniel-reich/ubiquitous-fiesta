
import re
plus_sign=lambda t:re.findall(r'(?=\+([a-z])\+)',t)==re.findall(r'[a-z]',t)

