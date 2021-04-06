
def is_it_true(relation):
  result = relation
  if '=' in relation:
    result = relation.replace('=', '==')
  return eval(result)

