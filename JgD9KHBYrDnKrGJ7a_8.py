
def swap_dict(dic):
  return {j: [x for x, y in dic.items() if y == j] for i, j in dic.items()}

