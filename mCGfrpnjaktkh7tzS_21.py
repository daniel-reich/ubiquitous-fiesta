
def is_it_true(relation):
  if "=" in relation:
    return eval(relation.replace("=","=="))
  return eval(relation)

