
import re
txt = '... <!-- My -- comment test --> ..  <!----> .. '
pattern = '<\!.+?>'
re.findall(pattern, txt)

