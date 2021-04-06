
import re
valid_rondo=lambda s:len(s)>2and re.findall(r'(?=A(\w|'')A)',s)==list(re.sub('A','',s))

