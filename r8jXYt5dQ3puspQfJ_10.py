
def split(txt):
  return "".join(
    [c for c in txt if c in "aeiou" ] + [c for c in txt if c not in "aeiou"]
  )

