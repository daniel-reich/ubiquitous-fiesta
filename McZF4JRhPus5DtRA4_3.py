
def dna_to_rna (dna):
  return (
    dna.replace('A','U')
    .replace('T','A')
    .replace('C','X')
    .replace('G','C')
    .replace('X','G'))

