
from collections import defaultdict
faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
class Card:
  def __init__(self, istr):
    self.string = istr.lower()
    self.face = self.string[:-1]
    self.suit = self.string[-1]
​
  def __lt__(self, other):
    return faces.index(self.face) < faces.index(other.face)
​
  def __eq__(self, other):
    return self.face == other.face and self.suit != other.suit
​
def poker_hand_ranking(hand):
  hand = sorted(Card(card) for card in hand)
  if len(set([card.suit for card in hand])) == 1:
    if [card.face for card in hand] == faces[-5:]: return "Royal Flush"
    elif [card.face for card in hand] == faces[faces.index(hand[0].face):faces.index(hand[-1].face)+1]: return "Straight Flush"
  hand_faces = defaultdict(int)
  hand_suits = defaultdict(int)
  for card in hand:
    hand_faces[card.face] += 1
    hand_suits[card.suit] += 1
  hfv, hsv = list(hand_faces.values()), list(hand_suits.values())
  if 4 in hfv: return "Four of a Kind"
  elif 3 in hfv and 2 in hfv: return "Full House"
  elif 5 in hsv: return "Flush"
  elif [card.face for card in hand] == faces[faces.index(hand[0].face):faces.index(hand[-1].face)+1]: return "Straight"
  elif 3 in hfv: return "Three of a Kind"
  elif hfv.count(2)==2: return "Two Pair"
  elif hfv.count(2)==1: return "Pair"
  return "High Card"

