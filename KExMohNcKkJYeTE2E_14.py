
def is_orthogonal(first, second):
  retval = 0
  for i in range(len(first)):
    retval += first[i]*second[i]
  return retval==0

