
def society_name(friends):
  friends.sort()
  name = ""
  for i in friends:
    name += i[0]
  return name

