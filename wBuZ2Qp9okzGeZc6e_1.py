
def first_place(road):
  for char in reversed(road):
    if char != '=':
      return char

