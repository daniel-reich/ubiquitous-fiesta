
def swap_cards(n1, n2):
  
  class Game:
    class Hand:
      class Card:
        
        def __init__(self, val, place):
          self.v = val
          self.p = place
        
        def swap(self, other):
          
          gv = self.v
          tv = other.v
          
          gp = self.p
          tp = other.p
          
          self.v = tv
          self.p = tp
          
          other.v = gv
          other.p = gp
          
          return True
      
      def __init__(self, cards):
        self.cards = list(str(cards))
        
        self.tens = Game.Hand.Card(self.cards[0], 10)
        self.ones = Game.Hand.Card(self.cards[1], 1)
        
        if self.tens.v > self.ones.v:
          self.lowest = 1
        else:
          self.lowest = 10
​
      def card_swap(self, self_p, other, other_p):
      # print(34)
        if self_p == 10:
          self_card = self.tens
        elif self_p == 1:
          self_card = self.ones
        else:
          return 'Incorrect position given for SP: {}'.format(self_p)
      # print(41)
        if other_p == 10:
          other_card = other.tens
        elif other_p == 1:
          other_card = other.ones
        else:
          return 'Incorrect position given for OP: {}'.format(other_p)
      # print(48)
        self_card.swap(other_card)
      # print(50)
        return True
    
      def inspect_card(self, p):
        
        if p == 10:
          return [self.tens.v, self.tens.p]
        elif p == 1:
          return [self.ones.v, self.ones.p]
        else:
          return 'Incorrect position given for P: {}'.format(p)
      
      def victory(self, other):
        
        return (self.tens.v * 10 + self.ones.v) > (other.tens.v * 10 + other.ones.v)
    
    def __init__(self, hand1, hand2):
      self.h1 = Game.Hand(hand1)
      self.h2 = Game.Hand(hand2)
      #print(self.h1, self.h2)
    def cards_swap(self, player, card_remove, card_take):
      if player == 1:
      # print(player, card_remove, card_take)
        self.h1.card_swap(card_remove, self.h2, card_take)
      elif player == 2:
        self.h2.card_swap(card_remove, self.h1, card_take)
      else:
        return 'Incorrect player: {}'.format(player)
    
    def victor(self):
      
      v1 = self.h1.victory(self.h2)
      v2 = self.h2.victory(self.h1)
      
      if v1 == True:
        return 1
      elif v2 == True:
        return 2
      else:
        return 0
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  card_game = Game(n1, n2)
  card_game.cards_swap(1,card_game.h1.lowest,10)
  return card_game.victor() == 1

