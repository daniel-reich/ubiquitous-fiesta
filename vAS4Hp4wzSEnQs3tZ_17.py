
GUEST_LIST = {
  "Randy": "Germany", 
  "Karla": "France", 
  "Wendy": "Japan", 
  "Norman": "England", 
  "Sam": "Argentina"
}
​
def greeting(name):
  text = "Hi! I'm a guest."
  for x in GUEST_LIST:
    if name == x:
      text = "Hi! I'm {}, and I'm from {}.".format(name, GUEST_LIST.get(name))
  return text

