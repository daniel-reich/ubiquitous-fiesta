
import re
def swap_two(txt):
    return re.sub(r'(\w\w)(\w\w)', r"\2\1",txt)

