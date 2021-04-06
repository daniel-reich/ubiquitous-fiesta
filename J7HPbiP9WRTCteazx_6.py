
def n_differences(l):
  return l[0] if len(l) == 1 else n_differences([l[i+1]-l[i] for i in range(len(l[:-1]))])

