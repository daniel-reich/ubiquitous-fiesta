
def move_zeros(lst):
  arr = [x for x in lst if str(x)=="0" or str(x)=="0.0"]
  wbc = [str(x) for x in arr]
  cat = [x for x in lst if str(x) not in wbc]
  return cat + arr

