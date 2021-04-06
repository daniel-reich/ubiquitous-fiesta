
import re
unstretch = lambda s: re.sub(r'(.)\1*', r'\1', s)

