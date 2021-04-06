
def society_name(friends):
  soc_name = "".upper()
  friends.sort()
  for intial in friends:
    soc_name += intial[0]
  return soc_name

