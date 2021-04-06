
def who_goes_free(n, k):
  prisoners = [i for i in range(n)]
  step = 1
  to_del = []
  while len(prisoners) > 1:
    for item in prisoners:
      if step == k:
        to_del.append(item)
        step = 1
      else:
        step += 1
    for char in to_del:
      prisoners.remove(char)
    to_del = []
  return prisoners[0]

