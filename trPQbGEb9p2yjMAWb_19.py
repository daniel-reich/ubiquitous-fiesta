
def every_some(test, val, *args):
  return all(eval(str(i)+test) for i in args) if val == "everybody" else any(eval(str(i)+test) for i in args)

