
def correct_sentences(s):
  better1 = s.strip()
  better2 = better1[0].upper() + better1[1:]
  better3 = " ".join(better2.split())
  better4 = better3 + "."
  special = better4[1:]
  better5 = ""
  for x in special:
    if x.isupper() == True:
      better5 += ". "
    better5 += x
  almost = better4[0] + better5
  return almost.replace(" . ", ". ")

