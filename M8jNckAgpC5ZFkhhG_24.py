
def reverse_complement(input_sequence):
  res = ""
  for x in input_sequence:
    if x == 'A':
      res+="U"
    if x == 'U':
      res+="A"
    if x == "G":
      res+="C"
    if x == "C":
      res+= "G"
  return res[::-1]

