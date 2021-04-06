
def shift_sentence(string):                     # First letter shift
  """ Shift the first letter of each word to the right """
  string = string.split()
  first_letter = [x[0] for x in string][-1] + "".join([x[0] for x in string])[:-1]
  for i, x in enumerate(string):
    string[i] = first_letter[i] + x[1:]
  return " ".join(string)

