
def shuffle_count(num):
  
  class Deck:
    
    def __init__(self, cards):
      self.cards = cards
    
    def shuffle(self):
      
      half_point = len(self.cards)//2
      half1 = self.cards[:half_point]
      half2 = self.cards[half_point:]
      
      new_deck = []
      
      for n in range(len(half1)):
        new_deck.append(half1[n])
        new_deck.append(half2[n])
      #print(self.cards, new_deck)
      self.cards = new_deck
      return True
    
    def match(self, other):
      return self.cards == other.cards
  
  deck1 = Deck(list(range(1, 1 + num)))
  deck2 = Deck(list(range(1, 1 + num)))
  
  shuffles = 1
  deck1.shuffle()
  
  while deck1.match(deck2) != True:
    deck1.shuffle()
    shuffles += 1
  
  return shuffles

