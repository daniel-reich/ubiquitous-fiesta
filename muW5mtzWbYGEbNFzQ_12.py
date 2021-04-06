
def BMR(person):
  lis = list(person.keys())
  for i in lis:
    if i == "gender":
      a = person.get(i)
  if a == "male":
    total = person.get("size")*5.003+person.get("weight")*13.75+66.47-person.get("age")*6.755
  if a == "female":
    total = person.get("size")*1.85+person.get("weight")*9.563-4.676*person.get("age")+655.1
  c = person.get("sport")
  if c == 1:
    return round(total*1.2,1)
  elif c == 2:
    return round(total*1.375,1)
  elif c == 3:
    return round(total*1.55,1)
  elif c == 4:
    return round(total*1.725,1)
  elif c == 5:
    return round(total*1.9,1)

