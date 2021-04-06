
def cumulative_sum(lst):
  additive_list = [0]
  for n in range(len(lst)):
    additive_list.append(lst[n]+additive_list[n])
  additive_list.remove(0)
  return additive_list

