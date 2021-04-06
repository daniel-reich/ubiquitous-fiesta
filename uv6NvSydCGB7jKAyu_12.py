
def is_parsel_tongue(sentence):
  lwrstnc = ''
  for i in sentence:
    lwrstnc += i.lower()
  lwrlst = lwrstnc.split()
  tracker = 1
  for j in lwrlst:
    sticker = 0
    ssticker = 0
    if 's' in j:
      sticker += 1
    for k in range(len(j)-1):
      if j[k] == 's' and j[k+1] == 's':
        ssticker += 1
    if sticker <= ssticker:
      tracker *= 1
    else:
      tracker *= 0
  return tracker == 1

