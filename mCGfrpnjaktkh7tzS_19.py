
def is_it_true(relation):
  chg = relation.replace('=', '==')
  return eval(chg)

