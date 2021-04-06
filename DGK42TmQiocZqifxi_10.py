
def reverse_complement(input_sequence):
  dic = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
  lis = [dic[i] for i in input_sequence]
  lis.reverse()
  return ''.join(lis)

