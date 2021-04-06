
def get_name(address):
  name = ""
  for letter in address:
    if letter == '@':
      break
    elif letter.isalpha():
      name += letter
  return name

