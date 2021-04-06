
def sigilize(desire):
  vowels = "AEIOU"
  desire = desire.upper().replace(' ','')
  sigil=''
  for i in range(len(desire)):
    if desire[i] not in vowels:
      if desire[i] not in desire[i+1:]:
        sigil+=desire[i]
  return sigil

