
def poker_hand_ranking(hand):
      
  cards = [x[:-1] for x in hand]
  postupnost = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  highest_straight = (set(cards) == {"10", "J", "Q", "K", "A"})
  min_index = min([postupnost.index(x) for x in cards])
  straight = True
  
  for i in range(1,5):
      if postupnost[min_index+i] in set(cards):
          continue
      else:
          straight = False
              
  # Four of a kind
      
  four = False
      
  for card in cards:
      if cards.count(card) == 4:
          four = True
          break
  
  # Fullhouse
  fh_list = [cards.count(card) for card in cards] 
  fullhouse = (fh_list.count(3) == 3) and (fh_list.count(2) == 2)    
​
  same_color = (lambda hand: (hand[0][-1] == hand[1][-1] == hand[2][-1] == hand[3][-1] == hand[4][-1]))(hand)
  
  if same_color and highest_straight:
      return "Royal Flush"
  
  if straight == True and same_color == True:
      return "Straight Flush"
  
  if four:
      return "Four of a Kind"    
      
  if same_color:
      return "Flush"
  
  if fullhouse:
      return "Full House"
         
  if straight:
      return "Straight"
  
  three = fh_list.count(3) == 3
  if three:
      return "Three of a Kind"
  
  twopair = fh_list.count(2) == 4   
  if twopair:
      return "Two Pair"
      
  onepair = fh_list.count(2) == 2   
  if onepair:
      return "Pair"    
  
  return "High Card"

