
def has_digit(txt):
  txtList = []
  for character in txt:
    txtList.append(character)
​
  for character in txtList:
    try:
      convert = int(character)
      return True
    except:
      continue
​
  return False

