
def every_some(test, req, *args):
  if req == 'everybody':
    return all(eval(str(arg)+test) for arg in args)
  else:
    return any(eval(str(arg)+test) for arg in args)

