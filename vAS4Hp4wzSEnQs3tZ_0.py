
GUEST_LIST = {
  "Randy": "Germany", 
  "Karla": "France", 
  "Wendy": "Japan", 
  "Norman": "England", 
  "Sam": "Argentina"
}
​
def greeting(name):
  return "Hi! I'm {}, and I'm from {}.".format(name, GUEST_LIST[name]) if name in GUEST_LIST.keys() else "Hi! I'm a guest."

