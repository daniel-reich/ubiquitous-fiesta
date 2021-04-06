
def reverse_complement(input_sequence):
  dic = {'A':'U', 'U':'A', 'C':'G','G':'C'}
  return ''.join([ dic[a] for a in input_sequence[::-1]] )

