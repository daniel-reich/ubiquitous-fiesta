
import re
replace_nums=lambda s:re.sub('\d+',lambda x:bin(int(x.group()))[2:],s)

