
def pentagonal(num):
  if num == 1:
    return 1
  return (num-1)*5 + pentagonal(num - 1)

