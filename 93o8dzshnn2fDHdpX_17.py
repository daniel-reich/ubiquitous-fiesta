
def lst_ele_sum(args):
  sums = []
  for n in range(len(args)):
    wo_arg = args[:n] + args[n+1:]
    sums.append(sum(wo_arg))
  return sums

