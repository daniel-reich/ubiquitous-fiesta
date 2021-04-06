
def gimme_the_letters(spectrum):
  a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  x,y=spectrum.split('-')
  return a[a.index(x):a.index(y)+1]

