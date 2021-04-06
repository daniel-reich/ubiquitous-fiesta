
def identify(*cube):
  a = sum(len(i)==len(cube) for i in cube)
  return "Full" if a == len(cube) else "Non-Full" if a == 0 \
      else "Missing {}".format(len(cube)-a)

