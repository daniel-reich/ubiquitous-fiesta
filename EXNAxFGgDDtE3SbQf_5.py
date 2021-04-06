
def shuffle_count(num, deck = None, count = 0):
  if deck == None:
    deck = list(range(1, num + 1))
  
  goal = list(range(1, num + 1))
  
  if count != 0:
    if goal == deck:
      return count
    
  left = deck[:num//2]
  right = deck[num//2:]
      
  count += 1
      
  shuffled = []
  
  for n in range(max(len(left), len(right))):
    try:
      shuffled.append(left[n])
    except IndexError:
      continue
    try:
      shuffled.append(right[n])
    except IndexError:
      continue
      
  return shuffle_count(num, shuffled, count)

