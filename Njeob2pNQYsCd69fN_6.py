
def prevent_distractions(txt):
  lst = ['anime','meme', 'vines', 'roasts', 'Danny', 'DeVito']
  for i in txt.split(' '):
    if i in lst:
      return 'NO!'
  return 'Safe watching!'

