
def is_it_true(relation):
  try:
    return eval(relation.replace("=","=="))
  except:
    return False

