
def reverse_complement(input_sequence):
  dic = {'A':'U','U':'A','G':'C','C':'G'}
  return ''.join(dic[i] for i in input_sequence)[::-1]

