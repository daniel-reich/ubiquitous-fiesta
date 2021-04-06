
def drange(*args):
  val = args[0]
  try: fin = args[1]
  except IndexError: fin = args[0]; val = 0
  try: it = args[2]
  except IndexError: it = 1
  out = []
  while val < fin:
    out.append(round(val,3))
    val += it
  return tuple(out)

