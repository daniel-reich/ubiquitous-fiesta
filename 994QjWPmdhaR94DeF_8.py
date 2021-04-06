
def get_birthday_cake(name, age):
  r="{ic} {age} Happy Birthday {name}! {age} {ic}".format(ic=["#","*"][age%2],age=age,name=name)
  return [["#","*"][age%2]*len(r),r,["#","*"][age%2]*len(r)]

