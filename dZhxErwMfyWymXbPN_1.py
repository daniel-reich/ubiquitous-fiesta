
def hangman(phrase, lst):
​
  class Hangman:
​
    def __init__(self, phrase):
      self.phrase = phrase
      words = phrase.split()
      self.shown = list(' '.join(['-' * len(w) for w in words]))
​
      for item in self.phrase:
        if item in '0123456789.!':
          self.shown[self.phrase.index(item)] = item
    
    def guess(self, l8r):
​
      indexes = []
​
      if l8r.lower() in self.phrase or l8r.upper() in self.phrase:
        for n in range(len(self.phrase)):
          if self.phrase[n] == l8r.lower() or self.phrase[n] == l8r.upper():
            indexes.append(n)
      
      for index in indexes:
        self.shown[index] = self.phrase[index]
      
      return True
  
  game1 = Hangman(phrase)
​
  for guess in lst:
    game1.guess(guess)
  
  return ''.join(game1.shown)

