
def dna_to_rna (dna):
  dic = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
  return ''.join([dic[char] for char in dna if char in dic])

