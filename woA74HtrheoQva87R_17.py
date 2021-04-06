
def concat(*args):
  n = len(args)
  final_list = []
  for i in range(n):
    for item in args[i]:
      final_list += [item]
  return final_list

