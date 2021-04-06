
def max_possible(n1, n2):
  new1 = [int(x) for x in str(n1)]
  new2 = [int(x) for x in str(n2)]
  new2 = sorted(new2)
  new2 = new2[::-1]
  
  m = min(len(new1),len(new2))
  
  c = 0
  for i in range(0, m):
    if new1[i] < new2[c]:
      new1[i] = new2[c]
      c += 1
  return int("".join(map(str, new1)))

