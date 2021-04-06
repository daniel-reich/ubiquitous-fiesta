
def accumulating_list(lst):
  return [
    sum(lst[:num])
    for num in range(1, len(lst) + 1)
  ]

