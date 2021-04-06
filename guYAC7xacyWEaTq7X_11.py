
def is_autobiographical(n):
  a=str(n)
  f=True
  for i in range (len(a)):
    if int(a[i])!=a.count(str(i)):
      f=False
      break
  return(f)

