
def remove_vowels(txt):
  k = ""
  for le in txt:
    if le=="a" or le=="e" or le=="u" or le=="o" or le=="i" or le=="A" or le=="E" or le=="U" or le=="O" or le=="I":
      continue
    else:
      k += le
  return k

