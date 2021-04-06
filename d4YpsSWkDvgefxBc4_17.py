
def over_twenty_one(cards):
  if 'A' not in cards: return sum([10 if x=='J' else 10 if x=='K' else 10 if x=='Q' else x for x in cards])>21
  else: a = sum([10 if x=='J' else 10 if x=='K' else 10 if x=='Q' else 0 if x=='A' else x for x in cards])
  return min(a+1, a+11)>21

