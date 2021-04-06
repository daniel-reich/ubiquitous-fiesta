
import re
​
pattern = ''.join('\\x'+'{:x}'.format(ord(c)) for c in 'edabit')

