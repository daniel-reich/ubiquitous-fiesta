
def letter_distance(txt1, txt2):
  return sum(
    abs(
      ord(char1) - ord(char2)
    ) for char1, char2 in zip(txt1, txt2)
  ) + abs(len(txt1) - len(txt2))

