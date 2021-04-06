
def skip_the_sugar(drinks):
  if len(drinks)>=0:
    return [n for n in drinks if n != "cola" and n!= "fanta"]
  else:
    return drinks

