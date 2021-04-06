
def BMR(person):
  if person['gender'] == 'male':
    formula = (66.47 + (13.75 * person['weight']) + (5.003 * person['size']) - (6.755 * person['age']))
  else:
    formula = (655.1 + (9.563 * person['weight']) + (1.85 * person['size']) - (4.676 * person['age']))
  sport = person['sport']
  if sport == 1:
    return round(formula * 1.2, 1)
  elif sport == 2:
    return round(formula * 1.375, 1)
  elif sport == 3:
    return round(formula * 1.55, 1)
  elif sport == 4:
    return round(formula * 1.725, 1)
  return round(formula * 1.9, 1)

