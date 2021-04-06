
def BMR(person):
  a = 0
  if person["gender"]=="male":
      a += 66.47+13.75*person["weight"]+5.003*person["size"]-6.755*person["age"]
  else:
      a += 655.1+9.563*person["weight"]+1.85*person["size"]-4.676*person["age"]
  if person["sport"]==1: return round(a * 1.2, 1)
  elif person["sport"]==2: return round(a * 1.375, 1)
  elif person["sport"]==3: return round(a * 1.55, 1)
  elif person["sport"]==4: return round(a * 1.725, 1)
  else: return round(a * 1.9, 1)

