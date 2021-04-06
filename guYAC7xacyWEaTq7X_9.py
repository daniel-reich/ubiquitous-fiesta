
def is_autobiographical(x):
  n = str(x)
  cnts = []
  for x in range(len(n)):
    cnts.append(n.count(str(x)))
  j = ''.join([str(x) for x in cnts])
  return n==j

