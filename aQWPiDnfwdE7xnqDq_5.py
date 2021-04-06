
def drange(*args):
  rounding = max(0 if pix < 0 else len(arg[pix+1:]) for pix, arg in [(str(arg).find('.'), str(arg)) for arg in args])
  current, limit = (0, args[0]) if len(args) == 1 else (args[0], args[1])
  step = 1 if len(args) < 3 else args[2]
  res = []
  while current < limit:
    res.append(round(current, rounding))
    current += step
  return tuple(res)

