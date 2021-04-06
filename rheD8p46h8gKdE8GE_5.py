
def grayscale(lst):
  return [[[round(sum(min((max((k, 0)), 255)) for k in j) / 3)] * 3 for j in i] for i in lst]

