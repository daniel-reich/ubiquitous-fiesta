
def bmr(person):
  if person.get('gender') == 'male':
    return 66.47 + (13.75 * person.get('weight')) + (5.003 * person.get('size')) - (6.755 * person.get('age'))
  return 655.1 + (9.563 * person.get('weight')) + (1.85 * person.get("size")) - (4.676 * person.get('age'))
​
def BMR(person):
  if person.get('sport') == 1:
    return round(bmr(person) * 1.2, 1)
  if person.get('sport') == 2:
    return round(bmr(person) * 1.375, 1)
  if person.get('sport') == 3:
    return round(bmr(person) * 1.55, 1)
  if person.get('sport') == 4:
    return round(bmr(person) * 1.725, 1)
  else:
    return round(bmr(person) * 1.9, 1)

