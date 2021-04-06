
def determine_who_cursed_the_most(d):
  me = 0
  spouse = 0
  for key,value in d.items():
    me += value["me"]
    spouse += value["spouse"]
  return "DRAW!" if me == spouse else "ME!" if me > spouse else "SPOUSE!"

