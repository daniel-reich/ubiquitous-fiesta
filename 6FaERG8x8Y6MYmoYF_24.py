
def dice_score(throw):
  points = sum(t*100 for t in set(throw) if throw.count(t) >= 3)
  if points == 100:
    points *= 10
  ones, fives = throw.count(1), throw.count(5)
  if ones > 3:
    points += (5-ones)*100
  elif ones < 3:
    points += ones*100
  if fives > 3:
    points += (5-fives)*50
  elif fives < 3:
    points += fives*50
  return points

