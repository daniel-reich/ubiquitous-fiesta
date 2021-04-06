
def dna_to_rna(dna):
  rna = ""
  for i in dna:
    if i == "A":
      rna = rna + "U"
    if i == "T":
      rna = rna + "A"
    if i == "G":
      rna = rna + "C"
    if i == "C":
      rna = rna + "G"
  return rna

