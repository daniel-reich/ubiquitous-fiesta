
# I should have re-worked the challenge! Just realised
# it can be solved by dividing the string lengths. I'll
# create a more challenging follow up.
def word_nest(word, nest):
  return len(nest) // len(word) - 1

