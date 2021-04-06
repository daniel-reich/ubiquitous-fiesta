
def dna_to_rna(dna):
  return ''.join([{'A':'U','T':'A', 'G':'C', 'C':'G'}[c] for c in dna])

