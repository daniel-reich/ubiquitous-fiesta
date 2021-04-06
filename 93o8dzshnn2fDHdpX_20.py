
def lst_ele_sum(args):
  total = sum(args)
  for i in range(len(args)):
    args[i] = total-args[i]
  return args

