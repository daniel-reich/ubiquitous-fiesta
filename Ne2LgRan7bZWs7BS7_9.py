
#Fix this code:
def get_container(product):
  matches = {
  "Bread" : "bag",
  "Milk" : "bottle",
  "Beer" : "bottle",
  "Eggs" : "carton",
  "Cerials" : "box",
  "Candy" : "plastic",
  "Cheese" : None
  }
  return matches[product]
print(get_container('Eggs'))

