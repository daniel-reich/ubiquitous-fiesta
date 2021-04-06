
import re
def count_missing_nums(l):
  l=list(map(int,re.findall('\d+',' '.join(l))))
  return sum(i not in l for i in range(min(l),max(l)))

