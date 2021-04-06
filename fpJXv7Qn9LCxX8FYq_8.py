
import re
def solve(eq):
  m = re.match(r'x\s([\-\+])\s(-?\d+)\s=\s(-?\d+)',eq)
  return eval(m.group(3)+m.group(1)+m.group(2)+'*-1')

