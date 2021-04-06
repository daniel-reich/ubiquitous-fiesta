
import string
​
def missing_alphabets(txt):
  a = {key:txt.count(key) for key in txt}
  m = max(a.values())
  return ''.join(i*(m-txt.count(i)) for i in string.ascii_lowercase if m-txt.count(i)>0)

