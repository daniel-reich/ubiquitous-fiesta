
def partially_hide(phrase):
  return ' '.join([word[0] + ''.join(['-' for i in word[1:-1]]) + word[-1] for word in phrase.split()])

