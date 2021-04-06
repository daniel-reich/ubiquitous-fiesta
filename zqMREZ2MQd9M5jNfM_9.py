
def is_symmetrical(num):
  num=str(num)
  f=num[::-1]
  if num==f:
    return bool(1)
  return bool(0)

