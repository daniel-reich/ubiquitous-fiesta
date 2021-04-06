
import re
find_longest=lambda s,recur=0: find_longest(re.split(r"\W",s),1) if recur==0 else s[0].lower() if len(s)==1 else find_longest(s[1:],1) if len(s[0])<len(s[1]) else find_longest([s[0]]+s[2:],1)

