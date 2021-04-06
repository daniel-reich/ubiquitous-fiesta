
def char_at_pos(characters, place):
  if type(characters) == list:
    placement = []
    for char in range(len(characters)):
      if (place == 'even') and (char % 2 != 0):
        placement.append(characters[char])
      elif (place == 'odd') and (char % 2 == 0):
        placement.append(characters[char])
  elif type(characters) == str:
    placement = ''
    for char in range(len(characters)):
      if (place == 'even') and (char % 2 != 0):
        placement += characters[char]
      elif (place == 'odd') and (char % 2 == 0):
        placement += characters[char]
  return placement

