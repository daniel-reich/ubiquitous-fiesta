
def increment_string(txt):
  if not any(x.isnumeric() for x in txt): return txt+'1'
  import re
  m = re.search(r'\d+$', txt)
  l = "%0" + str(len(m.group())) + 'd'
  return txt.split(m.group())[0] + (l % (int(m.group())+1))

