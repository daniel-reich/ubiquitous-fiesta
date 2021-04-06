
def grayscale(lst):
  return [[[round(sum((min(255, max(e, 0))) for e in elem)/3)] * 3 for elem in row]for row in lst]

