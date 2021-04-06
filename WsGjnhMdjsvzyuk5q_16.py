
def dashed(txt):
  return "".join(letter if letter not in "aeiouAEIOU" else "-" + letter + "-" for letter in txt)

