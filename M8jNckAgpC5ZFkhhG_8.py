
def reverse_complement(input_sequence):
  data = { 'A': 'U', 'G':'C', 'U':'A', 'C':'G'}
  comp = []
  for i in input_sequence:
    comp.append(data[i])
  return ''.join(comp[::-1])

