
def high_low(txt):
  lst = [int(char) for char in txt.split(" ")]
  return str(max(lst)) + " " + str(min(lst))

