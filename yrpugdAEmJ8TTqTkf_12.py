
def secret(num):
  first = int(str(num)[0])
  last = int(str(num)[-1])
  return (first**last) - (first*last)

