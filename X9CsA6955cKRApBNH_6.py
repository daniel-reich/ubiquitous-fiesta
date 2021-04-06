
def longest_run(lst):
  count = [0]
  tmp = [lst[0]]
  for i in lst[1:]:
    if abs(tmp[-1]-i) == 1 and i not in tmp:
      tmp.append(i)
      count[-1] += 1
    else:
      tmp = [i]
      count.append(0)
  return max(count) + 1

