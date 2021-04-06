
def stutter(word):
  ls = [i for i in word]
  ls = ls[0:2]
  return ls[0] + ls[1] + "... " + ls[0] + ls[1] +  "... " + word + "?"

