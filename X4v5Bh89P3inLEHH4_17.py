
def spin_around(l):
  r=l.count('right')
  l=l.count('left')
  return round(abs((r*90-l*90)/360),0)

