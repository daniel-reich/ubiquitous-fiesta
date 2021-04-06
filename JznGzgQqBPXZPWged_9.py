
def resist(net):
  net = eval(net)
  if type(net) == int or type(net) == float:
    return round(net, 1)
  if type(net) == tuple:
    return round(sum(resist(repr(n)) for n in net), 1)
  if type(net) == list:
    return round(1 / sum(1 / resist(repr(n)) for n in net), 1)

