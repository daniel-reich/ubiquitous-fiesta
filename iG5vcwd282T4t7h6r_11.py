
def str_to_dict(lst):
  A=[x.split('=') for x in lst]
  return {x[0]:x[1] for x in A}

