
def society_name(friends):
  friends.sort()
  name = []
  for friend in friends:
    name.append(friend[0])
  return ''.join(name)

