
def thirdthird(lst):
  try:
    return [i[2] for idx, i in enumerate(lst) if len(i) >=3 and idx == 2][0]
  except IndexError:
    return False

