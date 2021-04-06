
def reverse_complement(rna):
  return rna.translate(str.maketrans('AUGC','UACG'))[::-1]

