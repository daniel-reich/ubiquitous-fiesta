
import re
def valid(txt): return re.fullmatch('^(\d{4}|\d{6})',txt) != None

