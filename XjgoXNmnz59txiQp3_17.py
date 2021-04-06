
def split(number):
  if number > 6 or number == 1:
    threes = 3 ** (number // 3 - 1)
    first = 3 ** (number // 3) * (number % 3)
    second = round(threes * (number % 3 + 3))
    return [first, second][second > first]
  return 3 * (number - 3)

