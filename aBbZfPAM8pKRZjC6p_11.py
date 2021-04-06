
def fruit_salad(fruits):
  alp_len = list(len(x)//2 for x in fruits)
  return "".join(sorted(list(x[0:y] for x,y in zip(fruits,alp_len)) + list(list(x[y:] for x,y in zip(fruits,alp_len)))))

