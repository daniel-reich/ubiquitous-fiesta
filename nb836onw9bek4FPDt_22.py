
import re
p = r"[a-zA-Z]{2,}"
count_same_ends = lambda s: sum(1 if w[0]==w[-1] else 0 for w in re.findall(p,s.lower()))

