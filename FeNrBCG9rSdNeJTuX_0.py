
def max_possible(n1, n2):
  n1,n2 = list(str(n1)), sorted(list(str(n2)))
  for i in range(len(n1)):
    if n2 and n1[i]<n2[-1]:
      n1[i] = n2.pop()
  return int(''.join(n1))

