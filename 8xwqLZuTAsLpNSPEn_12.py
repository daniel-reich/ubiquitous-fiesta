
def award_prizes(names):
  points = [names[i] for i in names]
  points.sort(reverse=True)
  output = {}
  for i in names:
    if names[i] == points[0]:
      output[i] = 'Gold'
    elif names[i] == points[1]:
      output[i] = 'Silver'
    elif names[i] == points[2]:
      output[i] = 'Bronze'
    else:
      output[i] = 'Participation'
  return output

