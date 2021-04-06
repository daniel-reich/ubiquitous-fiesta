
def calculate_arrowhead(lst):
  ret = sum([(1*i.count('>'))+(-1*i.count('<')) for i in lst])
  return '>'*ret if ret>=0 else '<'*abs(ret)

