
def seven_boom(lst):
  store_string = ''
  for i in lst:
    store_string += str(i)
  for i in store_string:
    if i == "7":
      return "Boom!"
  return "there is no 7 in the list"

