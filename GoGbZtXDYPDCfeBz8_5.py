
def magic(txt):
  date = txt.split(" ")
  product = int(date[0]) * int(date[1])
  if product == int(date[2][-len(str(product)):]):
    return True
  return False

