
def is_it_true(relation):
  if "=" in relation:
    relation = relation.replace("=", "==")
  return eval(relation)

