
def missing_alphabets(txt):
  freqlist = []
  result = ''
  for i in range(26):
    freqlist.append(txt.count(chr(i+97)))
    
  for i in range(0, len(freqlist)):
    if freqlist[i] < max(freqlist):
      char = chr(i+97)
      result = result + char * (max(freqlist) - freqlist[i])
      
  return result

