
def lst_ele_sum(args):
  return [sum(args[:i]+args[i+1:]) for i in range(len(args))]

