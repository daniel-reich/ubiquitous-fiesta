
def every_some(test, val, *n):
  return [any, all]["v" in val](eval(str(m) + test) for m in n)

