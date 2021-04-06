
def reverse_odd(txt):
  return " ".join([l[::-1] if len(l)%2==1 else l for l in txt.split()])

