
def determine_who_cursed_the_most(d):
  me=0
  spouse=0
  for n,i in d.items():
    me+=i["me"]
    spouse+=i["spouse"]
      
  print(me,spouse)
  if me>spouse:
    return "ME!"
  elif me<spouse:
    return "SPOUSE!"
  else:
    return "DRAW!"

