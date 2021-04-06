
def identify(*cube):
  num_ls = [len(i) for i in cube]
  if max(num_ls) != len(cube):
    if sum(num_ls) == len(cube)*max(num_ls):
      return "Non-Full"
    else:
      return "Missing {}".format(len(cube)*max(num_ls)-sum(num_ls))
  else:
    if sum(num_ls) == pow(len(cube),2):
      return "Full"
    else:
      return "Missing {}".format(pow(len(cube),2)-sum(num_ls))

