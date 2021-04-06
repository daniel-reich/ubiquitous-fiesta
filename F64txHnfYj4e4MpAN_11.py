
def schoty(frame):
  indicies = [
    i.index('-')
    for i in frame
  ]
  return sum(
    j * 10 ** i
    for i, j in enumerate(reversed(indicies))
  )

