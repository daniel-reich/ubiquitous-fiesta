
def split(number):
  threes = number // 3
  remainder = number - (3 * threes)
  if threes == 0:
    return remainder
  elif threes == 1:
    return (3 * threes) * remainder
  else:
    if remainder == 0:
      return 3 ** threes
    elif remainder == 1:
      return 4 * (3 ** (threes - 1))
    else:
      return 2 * (3 ** threes)

