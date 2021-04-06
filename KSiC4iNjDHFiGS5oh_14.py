
def is_super_d(n):
  res = [str(d) * d in str(d * n ** d) for d in range(2, 10)]
  try:
    return "Super-{} Number".format(res.index(True) + 2)
  except ValueError:
    return "Normal Number"

