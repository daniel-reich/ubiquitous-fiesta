
def age_difference(ages):
  [a, b, *_] = sorted(ages, reverse=True)
  return 'No age difference between spouses.' if a == b else \
    "{} {}".format(a - b, 'years' if a - b > 1 else 'year')

