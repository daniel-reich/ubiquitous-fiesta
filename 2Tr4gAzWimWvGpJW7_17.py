
def is_there_consecutive(lst, n, times):
  if times==0:
    return n not in lst
  lst = ''.join([str(i) for i in lst])
  n = str(n)*times
  return n in lst

