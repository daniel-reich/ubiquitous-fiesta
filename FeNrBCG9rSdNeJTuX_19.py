
def max_possible(n1, n2):
  n1 = list(str(n1))
  n2 = sorted(list(str(n2)))
  n2 = list(reversed(n2))
  for i in range(len(n1)):
    if n2 == []:
      break
    if n1[i] < n2[0]:
      n1[i] = n2[0]
      n2 = n2[1:]
  retstr = ""
  for i in n1:
    retstr += i
  return(int(retstr))

