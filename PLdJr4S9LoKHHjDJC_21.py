
def identify(*cube):
  lengths = sorted([len(x) for x in cube])
  if not lengths[0] == lengths[-1] == len(lengths):
    if lengths[0] == lengths[-1]:
      return "Non-Full"
    else:
      return "Missing {}".format(abs(len(lengths)**2 - sum(lengths)))
  else:
    return "Full"

