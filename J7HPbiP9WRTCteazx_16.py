
def n_differences(l):
  if len(l) < 2: return l[0]
  return n_differences([l[i+1] - l[i] for i in range(len(l)-1)])

