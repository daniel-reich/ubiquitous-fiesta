
def multiply(n1, n2):
  total = 0
  if n1 < 0 and n2 < 0:
    for i in range(abs(n1)):
      total += abs(n2)
    return total
  if n1 < 0:
    for i in range(abs(n1)):
      total += n2
    return int('-{}'.format(total))
  elif n2 < 0:
    for i in range(abs(n1)):
      total += abs(n2)
    return int('-{}'.format(total))
  else:
    for i in range(n1):
      total += n2
    return total

