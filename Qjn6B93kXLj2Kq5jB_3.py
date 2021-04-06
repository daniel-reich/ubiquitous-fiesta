
def simplify_frac(f):
  lst = [int(foo) for foo in f.split("/")]
  for foo in range(2, min(lst) + 1):
    while True:
      if not lst[0] % foo and not lst[-1] % foo:
        lst[0] //= foo
        lst[-1] //= foo
      else:
        break
  return "{}/{}".format(*lst)

