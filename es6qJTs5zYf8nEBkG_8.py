
def is_rectangle(coordinates):
  xs = [eval(x)[0] for x in coordinates]
  ys = [eval(x)[1] for x in coordinates]
  return len(set(xs)) == len(set(ys)) == 2 and len(set(coordinates)) == 4

