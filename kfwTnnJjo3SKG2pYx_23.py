
def replace_nums(string):
  import re
  def digitrepl(match):
    value = int(match.group())
    return getBin(value)
    
  def getBin(i =0):
    s = []
    j=i
    if i == 0:
      return '0'
    else:
      while j > 0:
        s.append( j % 2 )
        j= j // 2
      return ''.join(str(k) for k in reversed(s))
  p = re.compile(r'\d+')
  return p.sub(digitrepl,string)

