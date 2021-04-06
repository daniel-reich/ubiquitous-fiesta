
def reverse_complement(input_sequence):
  table = str.maketrans("AGCU","UCGA")
  return input_sequence.translate(table)[::-1]

