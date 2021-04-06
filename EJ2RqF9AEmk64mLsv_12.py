
def lottery(t, w):
  a = len([i for i in t if chr(i[1]) in i[0]])
  return 'Loser!' if a<w else 'Winner!'

