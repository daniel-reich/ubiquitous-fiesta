
def get_primiera_score(deck):
  if len(set([x[1] for x in deck])) != 4: return 0
  score = 40
  cards = ["s", "c", "d", "h"]
  for i in cards:
    if "7"+i in deck: score += 11
    elif "6"+i in deck: score += 8
    elif "A"+i in deck: score += 6
    elif "5"+i in deck: score += 5
    elif "4"+i in deck: score += 4
    elif "3"+i in deck: score += 3
    elif "2"+i in deck: score += 2
  return score

