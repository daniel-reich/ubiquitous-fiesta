
def reverse_complement(input_sequence):
  dct = {'A':'U','U':'A','G':'C','C':'G'}
  return ''.join(dct[c] for c in input_sequence)[::-1]

