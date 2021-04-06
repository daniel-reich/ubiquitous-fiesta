
def security(txt):
  for i in range(len(txt)):
    if txt[i]=='T':
      for j in range(len(txt)):
        if txt[j]=='$' and 'G' not in txt[i:j] and 'G' not in txt[j:i]: return 'ALARM!'
  return 'Safe'

