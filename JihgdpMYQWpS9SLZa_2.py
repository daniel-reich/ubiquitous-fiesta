
def score31(c1, c2, c3):
  
  suit_points = {'D': 0, 'H': 0, 'S': 0, 'C': 0}
  nums = []
  
  for card in [c1, c2, c3]:
    suit = card[0]
    try:
      val = int(card[1:])
      nums.append(val)
    except ValueError:
      val = 10 if card[1:] != 'A' else 11
      nums.append(card[1:])
    suit_points[suit] += val
  
  if len(list(set(nums))) == 1:
    return 32 if nums[0] == 'A' else 30.5
  
  return max(suit_points.values())

