
def dna_to_rna(dna):
  d={'A':'U','T':'A','G':'C','C':'G'}
  return "".join(d[x] for x in dna)

