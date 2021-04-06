
def first_place(road):
  if not road.replace("=","").isalpha():
    return None
  return road.replace("=","")[-1]

