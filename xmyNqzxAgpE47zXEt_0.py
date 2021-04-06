
import re
is_alphabetically_sorted=lambda s:any(len(x)>2and x==''.join(sorted(x))for x in re.findall(r'[\w]+',s))

