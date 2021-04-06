
def reverse(txt):
  reversed = ""
  for letter in txt:
    reversed = letter + reversed
  return reversed

