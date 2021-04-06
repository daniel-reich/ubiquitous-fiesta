
def dna_to_rna(dna):
  rna = []
  for let in dna:
    if let == 'A':
      let = 'U'
      rna.append(let)
    elif let == 'T':
      let = 'A'
      rna.append(let)
    elif let == 'G':
      let = 'C'
      rna.append(let)
    elif let == 'C':
      let = 'G'
      rna.append(let)
  return ''.join(rna)

