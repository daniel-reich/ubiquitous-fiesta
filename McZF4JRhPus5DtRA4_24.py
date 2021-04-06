
def dna_to_rna(dna):
  dna_to_rna_dict =  {"A" :"U" , "T" :"A" , "C":"G" , "G":"C"}
  return "".join([dna_to_rna_dict.get(e) for e in dna])

