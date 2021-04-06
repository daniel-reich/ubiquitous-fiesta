
def reverse(txt):
  return ' '.join(i[::-1] if len(i) >= 5 else i for i in txt.split())

