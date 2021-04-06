
def my_sub(a, b):
  l1 = ["*"for i in range(a)]
  l2 = ["*"for i in range(b)]
  if b > a:
    return (len(l2[a:]))
  else :
    return (len(l1[b:]))

