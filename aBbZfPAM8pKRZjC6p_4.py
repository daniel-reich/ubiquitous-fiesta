
def fruit_salad(fruits):
  salad = []
  for f in fruits:
    salad.append(f[:len(f)//2])
    salad.append(f[len(f)//2:])
  return "".join(sorted(salad))

