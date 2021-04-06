
def is_symmetrical(num):
  src = str(num)
  j = -1
  for i in range(len(src)):
    if src[i] != src[j]:
      return False
    j -= 1
  return True

