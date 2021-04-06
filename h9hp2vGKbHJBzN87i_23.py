
def partially_hide(phrase):
  return " ".join([x[0]+(len(x)-2)*"-"+x[-1] for x in phrase.split()])

