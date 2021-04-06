
def super_reduced_string(txt):  
  for x in range(len(txt)-1):   
    if txt[x]==txt[x+1]:      
      return super_reduced_string(txt[:x]+txt[x+2:])  
  return txt if txt else 'Empty String'

