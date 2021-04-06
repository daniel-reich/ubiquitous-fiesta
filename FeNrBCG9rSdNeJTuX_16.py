
def max_possible(n1, n2):
  n1, n2 = list(str(n1)), list(str(n2))
  for i in range(len(n1)):
    bigger = None
    for j in n2:
      if j > n1[i]:
        n1[i] = j
        bigger = j
    if bigger:
      n2.remove(bigger)
  return int(''.join(n1))

