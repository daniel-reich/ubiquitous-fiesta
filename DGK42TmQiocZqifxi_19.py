
def reverse_complement(input_sequence):
  dic = {'A' : 'U', 'G' : 'C', 'U': 'A', 'C': 'G'}
  RNA = ''.join([dic.get(i) for i in input_sequence])
  return RNA[::-1]

