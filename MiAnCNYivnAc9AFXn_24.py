
def value(char):
  if type(char) == str:
    if char.isdigit():
      return "{}!".format(char)
    else:
      return "{}!".format(char.capitalize())
  elif type(char) == int:
    if char % 2 == 0:
      return char + 1
    else:
      return char
  elif char == True:
    return False
  else:
    return True
  
def change_types(lst):
  new_list = [value(char) for char in lst]
  return new_list

