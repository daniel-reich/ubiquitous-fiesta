
def fruit_salad(fruits):
  a=[i[:len(i)//2] for i in fruits]
  b=[i[len(i)//2:] for i in fruits]
  return ''.join(sorted(a+b))

