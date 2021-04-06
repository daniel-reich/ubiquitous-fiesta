
def flip_end_chars(txt):
  if len(txt) < 2 or not isinstance(txt, str):
    return "Incompatible."
  if txt[0] == txt [-1]:
    return "Two's a pair."
  return txt [-1] + txt [1:-1] + txt [0]
​
#If the length of the string is less than two, return "Incompatible.".
#If the argument is not a string, return "Incompatible.".
#If the first and last characters are the same, return "Two's a pair.".

