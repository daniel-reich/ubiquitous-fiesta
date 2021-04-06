
def straight_digital(number):
  if number >= 100:
    if len(set(str(number))) == 1:
      return "Trivial Straight"
    x = [int(b) - int(a) for b, a in zip(str(number)[1:], str(number))]
    return x[0] if len(set(x)) == 1 else 'Not Straight'
  return 'Not Straight'

