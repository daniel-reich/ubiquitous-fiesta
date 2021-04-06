
def lst_ele_sum(args):
  return [sum(args[j] for j in range(len(args)) if args[j] != i) for i in args]

