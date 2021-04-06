
def reverse_complement(input_sequence):
  myDict = {
    'A':'U',
    'C':'G',
    'G':'C',
    'U':'A'
  }
  lst = []
  for c in input_sequence:
    lst.insert(0, myDict[c])
  return ''.join(lst)

