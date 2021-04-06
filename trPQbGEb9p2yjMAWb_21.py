
def every_some(test, val, *a):
  x = [eval(str(i)+test) for i in a]
  return eval(("all" if "v" in val else "any")+"(x)")

