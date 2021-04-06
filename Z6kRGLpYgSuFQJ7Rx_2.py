
import re
find_longest=lambda s:max(re.findall(r'\w+',s.lower()),key=len)

