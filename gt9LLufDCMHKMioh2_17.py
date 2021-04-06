
def stutter(word):
  short_word = ""
  for i in range(2):
    short_word += (word[i])
  stutter_string = short_word + "... " + short_word + "... "
  full_string = stutter_string + word + "?"
  return full_string

