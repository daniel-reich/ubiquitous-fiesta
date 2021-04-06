
def dna_to_rna(dna):
  dna1 = dna.maketrans("TCGA", "AGCU")
  return dna.translate(dna1)

