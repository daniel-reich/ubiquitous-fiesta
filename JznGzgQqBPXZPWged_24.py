
def resist(net):
  def a(*data):
    return sum([x for x in data])
  def b(*data):
    return 1/sum([1/x for x in data])
  
  tmp=net.replace('(','a(').replace('[','b(').replace(']',')')
  print(tmp)
​
  return round(eval(tmp),1)

