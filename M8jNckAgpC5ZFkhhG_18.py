
def reverse_complement(input_sequence):
  a = ""
  for letter in input_sequence:
    if letter == "U":
      a += "A"
    elif letter == "A":
      a += "U"
    elif letter == "G":
      a += "C"
    elif letter == "C":
      a += "G"
  return a[::-1]

