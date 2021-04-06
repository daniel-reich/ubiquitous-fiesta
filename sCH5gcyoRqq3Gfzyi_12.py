
import re
def valid_str_number(s):
    return bool(re.fullmatch('\d*\.?\d*', s))

