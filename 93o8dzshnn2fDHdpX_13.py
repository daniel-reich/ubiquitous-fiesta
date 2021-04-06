
def lst_ele_sum(args):
  return [
    sum(num for num_index, num in enumerate(args) if num_index != index)
    for index, num in enumerate(args)
  ]

