
def is_it_true(relation):
  relation = relation.replace("=", "==")
  return eval(relation)

