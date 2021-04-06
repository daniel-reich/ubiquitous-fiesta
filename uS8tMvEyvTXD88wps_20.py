
def reverse(txt):
  return ' '.join(i if len(i) < 5 else i[::-1] for i in txt.split())

