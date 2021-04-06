
def split_code(item):
  numbers = ""
  apl = ""
  for i in item:
    if i.isalpha():
      apl += i
    else:
      numbers += i
  return [apl, int(numbers)]

