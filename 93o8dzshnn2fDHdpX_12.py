
def lst_ele_sum(args):
  return [sum(args[i+1:]+args[:i]) for i in range(len(args))]

