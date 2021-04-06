
def is_it_true(relation):
  if '=' not in relation:
    return eval(relation)
  else:
    return eval(relation.replace('=', '=='))

