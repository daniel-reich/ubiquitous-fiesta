
def dna_to_rna (dna):
  return dna.translate(str.maketrans('ATCG','UAGC'))

