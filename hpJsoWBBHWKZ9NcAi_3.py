
import re
def bird_code(lst):
  x = [re.findall('[A-Z][a-z]+', i) for i in lst]
  return [(''.join([j[:2 if len(i)==2 else 4 if len(i)==1 else 1] for j in i] + [i[-1][1:]])[:4]).upper() for i in x]

