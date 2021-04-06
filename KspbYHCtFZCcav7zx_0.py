
def bill_split(spicy, cost):
  friend = sum([x[1] for x in list(zip(spicy, cost)) if x[0] == 'N'])/2
  you = sum(cost)-friend
  return [you, friend]

