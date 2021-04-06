
def is_rectangle(coordinates):
  if len(coordinates) != 4:
    return False
  elif len(coordinates) != len(set(coordinates)):
    return False
  else:
    numbers = []
    for elements in coordinates:
      for char in elements:
        if char.isdigit():
          numbers.append(int(char))
    if len(set(numbers)) <= 4:
      return True
    else:
      return False

