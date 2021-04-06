
def generate_word(n):
  if n<2: return 'invalid'
  if n==2: return 'b, a'
  meh = generate_word(n-1)
  return meh + ', ' + ''.join(meh.split(', ')[-2:])

