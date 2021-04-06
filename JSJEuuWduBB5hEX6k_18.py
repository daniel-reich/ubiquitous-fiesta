
def XO(text):
  return sum([1 for e in text if e in 'xX']) == sum([1 for e in text if e in 'oO'])

