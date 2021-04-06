
def bracket_logic(xp):
  current = []
  openingBrackets = ["(", "[", "<", "{"]
  closingBrackets = {")":0, "]":1, ">":2, "}":3}
  for char in xp:
    if char in openingBrackets:
      current.append(char)
    if char in closingBrackets:
      if current[-1] != openingBrackets[closingBrackets[char]]:
        return False
      else:
        current.pop()
  if len(current):
    return False
  return True

