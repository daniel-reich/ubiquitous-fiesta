
def remove_numbers(string):
  chars = list(string)
  print(chars)
  letters = []
  for char in chars:
    print(char)
    try: int(char)
    except: letters.append(char)
    
  return "".join(letters)

