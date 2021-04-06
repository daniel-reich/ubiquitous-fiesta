
def resist(nety):
  def res(net):
    if type(net) == tuple: return sum(res(sub) for sub in net)
    if type(net) == list: return 1/sum(1/res(sub) for sub in net)
    return net
​
  return round(res(eval(nety)),1)

