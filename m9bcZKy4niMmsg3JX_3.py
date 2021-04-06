
def society_name(friends):
  name=""
  friends.sort()
  for i in friends:
    name+=i[0]
  return name

