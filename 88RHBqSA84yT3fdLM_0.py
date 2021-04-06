
def inator_inator(s):
  return '{}{}inator {}000'.format(s, '-' if s[-1].lower() in 'aeiou' else '', len(s))

