
def dna_to_rna(dna):
  rna=''
  for i in range(len(dna)):
    if dna[i]=='A':
      rna+='U'
    if dna[i]=='T':
      rna+='A'
    if dna[i]=='G':
      rna+='C'
    if dna[i]=='C':
      rna+='G'
  return rna

