
def antipodes_average(lst):
  left = lst[:len(lst)//2]
  right = lst[len(lst)//2:]
  right.reverse()
  i = 0
  final = []
  while i < len(left):
    final.append((left[i] + right[i])/2)
    i += 1
  return final

