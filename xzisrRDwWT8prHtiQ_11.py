
def difference_two(lst):
  output = []
  lst = sorted(lst)
  for a in lst:
    for b in lst[1:]:
      if abs(a-b) == 2 and [b, a] not in output:
        output.append([a, b])
  return output

