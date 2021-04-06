
def dna_to_rna(dna):
  d = {'A':'U', 'T':'A', 'G':'C', 'C':'G'}
  return ''.join(d[i] for i in dna)

