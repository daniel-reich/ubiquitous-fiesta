
def reverse_complement(input_sequence):
  compAminoAcid = {'A' : 'U', 'U' : 'A', 'G' : 'C', 'C' : 'G'}
  complementaryStrandStraight = []
  complementaryStrand = ""
  for i in input_sequence:
      i = i.upper()
      complementaryStrandStraight.append(compAminoAcid[i])
  complementaryStrandStraight.reverse()
  for i in complementaryStrandStraight:
      complementaryStrand += i
  return complementaryStrand

