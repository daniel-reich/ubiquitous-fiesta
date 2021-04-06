
def first_place(road):
  try:
    return road.replace('=','')[-1]
  except:
    return None

