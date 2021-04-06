
def dna_to_rna(dna):
  tRNA = {"A": "U", "T": "A", "G": "C", "C": "G"}
  RNA = ""
  for nbase in dna:
    RNA += tRNA[nbase]
  return RNA

