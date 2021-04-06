
def list_of_multiples (num, length):
  count = 0
  x = []
  while len(x) < length:
    count += 1
    x.append(num*count)
  return x

