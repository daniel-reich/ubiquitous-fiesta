
import re
def portion_happy(n):
  n = ''.join(map(str,n))
  u = lambda x: len(re.findall("(?<!%s)%s(?!%s)"%(x,x,x),n))
  return 1-((u(0)+u(1))/len(n))

