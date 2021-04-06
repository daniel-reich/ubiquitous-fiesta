
def fruit_salad(fruits):
  a = []
  for i in fruits:
      a.append(i[len(i)//2:])
      a.append(i[:len(i)//2])
  return "".join(sorted(a))

