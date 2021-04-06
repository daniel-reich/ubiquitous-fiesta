
def reverse_complement(input_sequence):
  rev = {'A':'U','U':'A','C':'G','G':'C'}
  return ''.join(rev[i] for i in input_sequence)[::-1]

