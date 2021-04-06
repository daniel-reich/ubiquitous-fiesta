
def correct_stream(user, correct):
  mylist = []
  for x,y in zip(user,correct):
    if x == y:
      mylist.append(1)
    else:
      mylist.append(-1)
  return mylist

