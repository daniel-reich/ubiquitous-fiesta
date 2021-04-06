
def cars(wheels, bodies, figures):
  count = 0
  while all([wheels > 3, bodies > 0, figures > 1]):
    wheels -= 4
    bodies -= 1
    figures -= 2
    count += 1
  return count

