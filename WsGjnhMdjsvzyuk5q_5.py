
def dashed(txt):
  return "".join("-"+x+"-" if x in "AEIOUaeiou" else x for x in txt)

