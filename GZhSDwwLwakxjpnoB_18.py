
def thirdthird(lst):
  for idx, i in enumerate(lst):
    if idx == 2 and len(i) >= 3:
        return i[2]
  return False

