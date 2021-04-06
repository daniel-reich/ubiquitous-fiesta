
import re
txt = "242Edabit2345can3443be3254324addictive!"
pattern = "\D+"
''.join(re.findall(pattern, txt))

