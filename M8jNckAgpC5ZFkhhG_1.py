
def reverse_complement(input_sequence):
  return input_sequence.translate(str.maketrans('AUCG', 'UAGC'))[::-1]

