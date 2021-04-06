
GUEST_LIST = {
  "Randy": "Germany", 
  "Karla": "France", 
  "Wendy": "Japan", 
  "Norman": "England", 
  "Sam": "Argentina"
}
​
def greeting(name):
  if name not in GUEST_LIST:
    return "Hi! I'm a guest."
  else:
    return "Hi! I'm {}, and I'm from {}.".format(name, GUEST_LIST[name])

