
import re
def count_substring(s):
    return sum(len(re.findall(r"X", s[i:])) for i in range(len(s)-1) if s[i]=="A")

