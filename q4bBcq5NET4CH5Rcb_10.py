
def jay_and_bob(txt):
  d = {"half": .5, "quarter": .25, "eighth": .125, "sixteenth": .0625}
  num = str(round(28 * d[txt], 2))
  return "{} grams".format(num.split(".")[0] if num.endswith(".0") else num)

