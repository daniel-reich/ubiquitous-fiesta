
def award_prizes(names):
  places = sorted([(names[k], k) for k in names], reverse = True)
  names[places[0][1]] = "Gold"
  names[places[1][1]] = "Silver"
  names[places[2][1]] = "Bronze"
  for place in places[3:]:
    names[place[1]] = "Participation"
  return names

