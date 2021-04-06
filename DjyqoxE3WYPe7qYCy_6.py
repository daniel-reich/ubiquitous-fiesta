
def reverse_odd(txt):
  return ' '.join([i[::-1] if len(i)%2 else i for i in txt.split(' ')])

