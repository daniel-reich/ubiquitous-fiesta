
def society_name(friends):
  friends.sort()
  return "".join(list(map(lambda x: x[0], friends)))

