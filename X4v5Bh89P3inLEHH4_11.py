
def spin_around(lst):
  r=lst.count('right')
  l=lst.count('left')
  return abs(round(((r-l)*90)/360))

