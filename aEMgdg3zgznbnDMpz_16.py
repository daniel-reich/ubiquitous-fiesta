
def rotated_words(txt):
  dct = {"H":1, "I":1, "N":1, "O":1, "S":1, "X":1, "Z":1, "M":1, "W":1}
  def rotate(word):
    return 1 if all(dct.get(lt, 0) for lt in word) else 0
  
  return sum(rotate(word) for word in set(txt.split()))

