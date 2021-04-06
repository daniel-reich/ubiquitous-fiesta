
def pages_in_book(total):
  ret = [0]
  for i in range(1, 1400):
    ret.append(ret[-1]+i)
  return total in ret

