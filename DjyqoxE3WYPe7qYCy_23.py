
def reverse_odd(txt):
  return ' '.join(x[::-1] if len(x) % 2 !=0 else x for x in txt.split())

