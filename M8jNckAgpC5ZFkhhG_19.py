
def reverse_complement(input_sequence):
  complement = {"A": "U", "G": "C", "C": "G", "U": "A"}
  reverse = []
  reverse_complement = ""
  for i in input_sequence:
    reverse.insert(0, i)
  for x in reverse:
    reverse_complement += complement[x]
  return reverse_complement

