
def gimme_the_letters(x):
  arr = ''
  i = ord(x[0])
  while i <= ord(x[-1]):
    arr = arr + chr(i)
    i += 1
  return arr

