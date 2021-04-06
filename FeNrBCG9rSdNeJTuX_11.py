
def max_possible(n1, n2):
  n1 = list(str(n1))
  n2 = list(str(n2))
  for i in range(len(n1)):
    if n2 == []:
      break
    else:
      if max(n2) > n1[i]:
        n1[i] = max(n2)
        n2.remove(max(n2))
  return int("".join(n1))

