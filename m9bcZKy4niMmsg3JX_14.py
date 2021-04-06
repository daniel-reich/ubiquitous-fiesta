
def society_name(friends):
  socName = ''
  friends.sort()
  for item in friends:
    socName = socName + item[0]
  return socName

