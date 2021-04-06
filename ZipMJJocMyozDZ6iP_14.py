
def group(lst, size):
  return [[lst[j*round(len(lst)/size)+i] for j in range(size) if (j*round(len(lst)/size)+i)<len(lst)] for i in range(round(len(lst)/size))]

