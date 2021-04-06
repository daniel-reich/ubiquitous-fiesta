
def lst_ele_sum(args):
  return [sum(args[0:i]+args[i+1:]) for i in range(len(args))]

