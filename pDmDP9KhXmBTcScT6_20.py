
def get_name(address):
  name = ""
  for letters in address:
    if letters == "@":
      break
​
    elif letters.isalpha():
      name += letters
​
    else:
      continue
    
  return name

