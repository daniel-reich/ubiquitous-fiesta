
def validate(s):
  from re import findall
  return findall(
  r'^[+]?1?[ ]?[-/.(]?\d{3}[-/.)]?[ ]?\d{3}[-. /]?\d{4}$', s) != []

