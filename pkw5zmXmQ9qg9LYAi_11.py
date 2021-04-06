
import re
def space_message(txt):
  if "["in txt:
    a = re.findall(r'\[\d[A-Z]+\]',txt)
    for i in range(len(a)):
      txt = txt.replace(a[i],a[i][2:-1]*int(a[i][1]))
      return space_message(txt)
  else: 
    return txt

