
def shuffle_count(num):
  class Deck:
    
    def __init__(self, cards):
      self.cards = cards
      self.shuffles = 0
    
    def shuffle(self):
      
      first_half = self.cards[:int(len(self.cards)/2)]
      second_half = self.cards[int(len(self.cards)/2):]
      
      shuffled = []
      
      for n in range(max(len(first_half), len(second_half))):
        shuffled.append(first_half[n])
        shuffled.append(second_half[n])
      
      self.shuffles += 1
      self.cards = shuffled
      return True
    
    def __eq__(self, other):
      return self.cards == other.cards
  
  d1 = Deck(list(range(1, num+1)))
  d2 = Deck(list(range(1, num+1)))
  
  d1.shuffle()
  
  while d1 != d2:
    d1.shuffle()
  
  return d1.shuffles

