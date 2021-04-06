
def first_place(road):
  road = [i for i in road if i != '=']
  try:
    return road[-1]
  except:
    return None

