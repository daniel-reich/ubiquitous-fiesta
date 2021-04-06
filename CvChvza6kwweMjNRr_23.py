
def split_code(item):
  import re
  x = re.search(r'\d',item)
  y = x.span()
  return [item[0:y[1-1]]] + [int(item[y[1-1]:])]

