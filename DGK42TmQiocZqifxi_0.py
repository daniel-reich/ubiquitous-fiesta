
def reverse_complement(seq):  
  return seq.translate(str.maketrans('AUGC', 'UACG'))[::-1]

