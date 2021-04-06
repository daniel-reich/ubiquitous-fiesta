
def fruit_salad(fruits):
  chunks=[x[0:len(x)//2] for x in fruits]+[x[len(x)//2:] for x in fruits]
  return ''.join(sorted(chunks))

