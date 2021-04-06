
def over_twenty_one(cards):
  num_total = sum(i for i in cards if type(i) is int)
  face_total = sum(10 for i in cards if i in ('J', 'Q', 'K'))
  total = num_total + face_total
  return total + 11 > 21 and total + 1 > 21

