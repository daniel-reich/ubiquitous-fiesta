
def is_scalable(l):
  return max([l[i+1]- l[i] for i in range(len(l)-1)])<=5

