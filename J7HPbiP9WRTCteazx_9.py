
def n_differences(lst):
  final = []
  for i in range(len(lst)-1):
    final.append(lst[i+1]-lst[i])
  if len(final) == 1:
    return final[0]
  return n_differences(final)

