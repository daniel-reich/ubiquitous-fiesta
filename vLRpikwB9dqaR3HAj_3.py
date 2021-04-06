
def is_ord_sub(s,b):
  for x in s:
    if x not in b:return 0
    k=b.index(x)+1
    b=b[k:]
  return 1

