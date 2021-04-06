
def divisible_by_left(n):
  result = [False]
  for a, b in zip(str(n)[1:], str(n)):
    if int(b) != 0 and not int(a) % int(b):
      result.append(True)
    else:
      result.append(False)
  return result

