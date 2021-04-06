
def get_lucky_number(size, nth):
  a, s = range(1, size + 1), set([1])
  i = 2
  while len(a) > i:
    s.add(i)
    a1, av = [], 1
    for j in range(len(a)):
      if av == i:
        av = 1
      else:
        a1.append(a[j])
        av += 1
    a = a1[:]
    for k in a:
      if k not in s:
        i = k
        break
  return a[nth - 1]

