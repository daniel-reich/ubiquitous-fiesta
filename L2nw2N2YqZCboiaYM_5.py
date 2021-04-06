
import re
​
def repeated(s):
 return re.match(r"(\w+)\1+$", s) is not None

