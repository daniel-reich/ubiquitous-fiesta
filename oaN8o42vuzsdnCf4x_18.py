
def best_words(lst):
  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 2, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
  def scoreWord(word):
    return sum([score[i.lower()] for i in word])
    
  highest = 0
  for i in range(len(lst)):
    if scoreWord(lst[i]) > highest: highest = scoreWord(lst[i])
    
  return [w for w in lst if scoreWord(w) == highest]

