
import re
​
def tweet(txt):
  txt = re.sub(r'[.!,?]', '', txt)
  return ' '.join(i for i in txt.split() if i[0] == '@' or i[0] == '#')

