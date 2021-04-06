
def award_prizes(names):
  values = sorted(names.values())[::-1]
  for i in names:
    if names[i] == values[0]:
      names[i] = 'Gold'
    elif names[i] == values[1]:
      names[i] = 'Silver'
    elif names[i] == values[2]:
      names[i] = 'Bronze'
    else:
      names[i] = 'Participation'
  return names

