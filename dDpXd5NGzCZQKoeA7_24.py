
def num_args(f):
  c = 0
  try:
    f()
  except Exception as e:
    c = int(str(e).split()[2])
  return c

