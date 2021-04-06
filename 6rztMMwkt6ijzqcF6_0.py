
def is_repeated(st):
  for i in range(len(st),1,-1):
    if st == i*(st[:len(st)//i]):
      return i
  return False

