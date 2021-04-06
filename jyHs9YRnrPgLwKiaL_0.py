
def split(x):
  if x == 1:
    return 1
  return round(max((x/i)**i for i in range(2, x//2)), 1)

