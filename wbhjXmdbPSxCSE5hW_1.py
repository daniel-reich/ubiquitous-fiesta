
def sigilize(d):
  d = d.upper().replace(' ','')
  rem_dub = [d[i] for i in range(len(d)) if d[i] not in d[i+1:]]
  return ''.join(i for i in rem_dub if i not in 'AEIUO')

