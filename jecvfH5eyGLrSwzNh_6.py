
import re
​
def fauna_number(txt):
  info = re.findall('\d+ (?:muggercrocodile|one-hornedrhino|python|moth|monitorlizard|bengaltiger)', txt)
  return [tuple(i.split())[::-1] for i in info]

