
import re
txt = 'Hello!... Wait. How goes?..... GoodBye!..'
pattern = '\.{3,}'
re.findall(pattern, txt)

