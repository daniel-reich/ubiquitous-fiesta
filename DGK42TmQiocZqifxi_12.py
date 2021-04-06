
def reverse_complement(input_sequence):
  lst = [x for x in ''.join(input_sequence)]
  word = ''
  for n in lst[::-1]:
    if n == "C":
      word += "G"
    elif n == "G":
      word += "C"
    elif n == "A":
      word += "U"
    elif n == "U":
      word += "A"
  return word

