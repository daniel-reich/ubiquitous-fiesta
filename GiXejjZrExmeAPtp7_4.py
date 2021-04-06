
def fifth(*args):
  myans = []
  for i in args:
    myans.append(i)
  if len(myans) < 5:
    return 'Not enough arguments'
  return type(myans[4])

