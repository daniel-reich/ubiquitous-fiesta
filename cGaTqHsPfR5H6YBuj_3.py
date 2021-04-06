
def make_sandwich(ingredients,flavor):
  lst = [['bread',i,'bread'] if i == flavor else [i] for i in ingredients]
  return [j for i in lst for j in i]

