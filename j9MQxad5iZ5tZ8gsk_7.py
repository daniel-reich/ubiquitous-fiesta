
def find_vertex(x):
  x = x.replace("x", "").replace(" + ", " ")
  x = [i for i in x.split(" ")]
  return -int(x[1]) // (2 * int(x[0]))

