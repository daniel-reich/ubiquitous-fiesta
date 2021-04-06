
def reverse_complement(input_sequence):
  string_a = "AGCU"
  string_b = string_a[::-1]
  trans = str.maketrans(string_a,string_b)
  return input_sequence[::-1].translate(trans)

