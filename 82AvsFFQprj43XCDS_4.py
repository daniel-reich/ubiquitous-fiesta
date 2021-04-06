
def no_strangers(txt):
  newtxt = [i.rstrip('"').rstrip(',').rstrip('.') for i in txt.lower().split(' ')]
  friend = []
  acq = []
  for i in range(len(newtxt)):
    if newtxt[:i].count(newtxt[i]) == 4:
      friend.append(newtxt[i])
  for j in range(len(newtxt)):
    if newtxt[:j].count(newtxt[j]) == 2 and newtxt[j] not in friend:
      acq.append(newtxt[j])
  return [acq, friend]

