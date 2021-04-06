
def schoty(frame):
  z = [''.join(str(len(y.split('---')[0]))) for y in frame]
  res = int(''.join([str(elem) for elem in z]))
  return res

