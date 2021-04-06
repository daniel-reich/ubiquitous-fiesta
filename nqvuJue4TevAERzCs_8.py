
import re
def has_digit(txt):
    search = re.findall('[0-9]',txt)
    return bool(search)

