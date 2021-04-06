
def every_some(test, val, *args):
  l = [eval(str(i)+test) for i in args]
  return all(l) if val=="everybody" else any(l)

