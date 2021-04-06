
def right_triangle(*args):
  if any( n<=0 for n in args ): return False
  else:
    args = sorted(args);
    return args[0]**2 + args[1]**2 == args[2]**2

