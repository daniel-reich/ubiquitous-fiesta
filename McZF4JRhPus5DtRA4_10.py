
def dna_to_rna(dna):
  return dna.translate(dna.maketrans("ATGC","UACG"))

