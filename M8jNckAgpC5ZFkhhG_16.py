
def reverse_complement(input_sequence):
  lstseq = list(input_sequence)
  converted_seq = []
  for x in lstseq:
    if x == 'A':  
      converted_seq += ["U"]
    elif x == 'U':
      converted_seq += ["A"]
    elif x == 'C':
      converted_seq += ["G"]
    elif x == 'G':
      converted_seq += ["C"]
  return (''.join(converted_seq))[::-1]

