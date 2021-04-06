
def maxofsuit(lst, suit):
  scale = {'2': 12, '3': 13, '4': 14, '5': 15, '6': 18, '7': 21, '8': 10,
      '9': 10, 'A': 16, 'J': 10, 'Q': 10, 'K': 10}
  return max([scale[card[0]] for card in lst if suit in card] + [0])
​
def get_primiera_score(deck):
  res = [maxofsuit(deck, s) for s in "cdhs"]
  return sum(res) if 0 not in res else 0

