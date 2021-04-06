
def count(deck):
  plusses = 0
  zeroes = 0
  negs = 0
  for card in deck:
        if card in [2,3,4,5,6]:
            plusses += 1
        elif card in [7,8,9]:
            zeroes += 1
        else:
            negs += 1
  return (plusses * 1)+ (zeroes * 0) + (negs * -1)

