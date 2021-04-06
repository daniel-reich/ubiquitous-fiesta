
def fruit_salad(fruits):
  salad = []
  for i in fruits:
    ind = len(i)//2
    salad.append(i[0:ind])
    salad.append(i[ind:])
  salad.sort()
  return ''.join(salad)

