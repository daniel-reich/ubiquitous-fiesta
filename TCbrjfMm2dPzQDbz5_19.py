
import re
​
def insert_whitespace(txt):
    lower = re.compile(r"[A-Z][a-z]+")
    return " ".join(lower.findall(txt))

