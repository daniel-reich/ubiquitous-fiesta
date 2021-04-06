
def my_sub(a, b):
  if a > b:
    mx = a
    mn = b
  elif a < b:
    mx = b
    mn = a
  elif a == b:
    return 0
  mn = (~mn) + 1
  return mx + mn

