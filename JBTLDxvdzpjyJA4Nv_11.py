
def super_reduced_string(txt):
  while any([i*2 in txt for i in txt]):
    for i in range(len(txt)-1):
      if txt[i]==txt[i+1]:
        txt = txt[:i]+txt[i+2:]
        break
  return txt if txt else 'Empty String'

