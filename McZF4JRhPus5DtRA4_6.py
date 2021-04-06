
def dna_to_rna(dna):
  
  d_to_r = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
  
  rna = ''
  
  for gene in dna:
    rna += d_to_r[gene]
  
  return rna

