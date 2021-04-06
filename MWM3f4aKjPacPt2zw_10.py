
def modify_last(txt, n):
  for x in range(n-1):
    txt += txt[-1]
  return txt

