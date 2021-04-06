
def count_smileys(x):
  import re
  y = ''.join(x)
  w = re.findall('[:;][-~]?[)D]', y)
  return len(w)

