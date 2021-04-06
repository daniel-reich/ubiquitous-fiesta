
def reverse_complement(sequence):
  return sequence[::-1].translate(str.maketrans('ACGU', 'UGCA'))

