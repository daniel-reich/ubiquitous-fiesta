
def count(n):
  if abs(n)<10:
    return 1
  return 1+count(abs(n)//10)

