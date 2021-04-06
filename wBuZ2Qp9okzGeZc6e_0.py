
def first_place(road):
  for i in road[::-1]:
    if i != '=':
      return i

