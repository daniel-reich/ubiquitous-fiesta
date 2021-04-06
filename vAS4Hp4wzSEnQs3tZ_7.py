
GUEST_LIST = {
  "Randy": "Germany", 
  "Karla": "France", 
  "Wendy": "Japan", 
  "Norman": "England", 
  "Sam": "Argentina"
}
​
def greeting(guest):
    if guest in GUEST_LIST:
       return "Hi! I'm"+" "+guest+", and I'm from "+ GUEST_LIST[guest] +"." 
​
    return "Hi! I'm a guest."

