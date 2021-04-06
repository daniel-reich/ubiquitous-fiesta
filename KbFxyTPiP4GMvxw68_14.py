
import re
def longest_zero(s):
    return max([match for match in re.findall("[0]+", s)]) if "0" in s else ""

