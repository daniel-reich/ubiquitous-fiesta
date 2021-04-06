
def word_builder(letters, positions):
  ref = {}
  for i in range(len(positions)): ref[positions[i]] = letters[i]
  a = ""
  # for value in ref.values():
  #   a += value
  return "".join(value for value in ref.values())
  return a

