
def dna_to_rna(dna):
  dic={ 
    "A":"U", "T":"A", "G":"C", "C":"G"
  }
  s=""
  for i in dna:
    if i in dic:
      s+=dic[i]
  return s

