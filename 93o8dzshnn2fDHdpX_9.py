
def lst_ele_sum(args):
  return [sum([args[i] for i in range(len(args)) if i!=j]) for j in range(len(args))]

