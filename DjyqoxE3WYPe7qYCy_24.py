
def reverse_odd(txt):
  return " ".join([w, w[::-1]][len(w) % 2] for w in txt.split())

