
def is_it_true(relation):
  a=0
  if "=" in relation:
    a = relation.index("=")
    return eval(relation[:a] +"="+ relation[a:])
  return eval(relation)

