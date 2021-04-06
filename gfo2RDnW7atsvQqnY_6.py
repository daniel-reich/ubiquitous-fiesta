
import re
def count_smileys(lst):
  return sum(bool(re.match("[:;][-~]?[D)]",i)) for i in lst)

