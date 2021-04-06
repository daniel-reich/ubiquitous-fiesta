
def lst_ele_sum(args):
  return [sum(args[:i]) + sum(args[i + 1:]) for i, _ in enumerate(args)]

