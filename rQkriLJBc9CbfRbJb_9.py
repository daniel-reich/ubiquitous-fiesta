
def index_of_caps(word):
  return [index for index, letter in enumerate(word) if letter == letter.upper() and letter.isalpha()]

