
import re
def prefix(exp):
  def evaluate(match):
    a,b,c,d,e = match.group(1,2,3,4,5)
    if a == "*":
      return str(int(c) * int(e))
    elif a == "+":
      return str(int(c) + int(e))
    elif a == "-":
      return str(int(c) - int(e))
    else:
      return str(int(c) // int(e))
    
  while True:
    try:
      return int(exp)
    except ValueError:
      exp = re.sub(r'([\+\-\*\/])(\s)(\-?\d+)(\s)(\-?\d+)',evaluate,exp)

