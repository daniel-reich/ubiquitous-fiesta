
def reverse_complement(input_sequence):
  d = {'A':'U',
  'U':'A',
  'G':'C',
  'C':'G'}
  
  return ''.join(d[i] for i in input_sequence)[::-1]

