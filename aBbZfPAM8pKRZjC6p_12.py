
def fruit_salad(fruits):
  return "".join(sorted([i[0:len(i)//2] for i in fruits] + [i[len(i)//2 if len(i)%2==0 else (len(i)//2):] for i in fruits]))

