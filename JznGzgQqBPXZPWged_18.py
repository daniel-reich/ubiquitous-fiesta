
def resist(net):
  if isinstance(net, str):
    return resist(eval(net))
  elif isinstance(net, tuple):
    return sum(resist(elem) for elem in net)
  elif isinstance(net, list):
    return round(1 / sum(1 / resist(elem) for elem in net), 1)
  else:
    return net

