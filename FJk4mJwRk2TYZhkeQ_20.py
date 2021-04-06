
def accum(txt):
  output = map(lambda x: x[1] * x[0], enumerate(list(txt),1))
  output = [x.capitalize() for x in output]
  return '-'.join(output)

