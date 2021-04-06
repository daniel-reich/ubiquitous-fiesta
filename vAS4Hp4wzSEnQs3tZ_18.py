
dict = {
  "Randy": "Germany", 
  "Karla": "France", 
  "Wendy": "Japan", 
  "Norman": "England", 
  "Sam": "Argentina"
}
​
def greeting(name):
  return "Hi! I'm {}, and I'm from {}.".format(name,dict[name]) if name in dict.keys() else "Hi! I'm a guest."

