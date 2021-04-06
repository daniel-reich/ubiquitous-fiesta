
def valid_str_number(n):
  dot = False
  for number in n:
    if number == ".":
      if dot == True:
        return False
      else:
        dot = True
        continue
    try:
      number = int(number)
    except:
      return False
  return True

