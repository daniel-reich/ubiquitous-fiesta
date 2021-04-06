
def final_countdown(lst):
  res = [lst.count(1), []]
  i = 0
  for _ in range(res[0]):
    i = lst.index(1, i) + 1
    j = i - 2
    while j >= 0:
      if not lst[j] == lst[j+1] + 1:
        break
      j -= 1
    res[1].append(lst[j+1:i])
  return res

