
def crack_pincode(pincode):
  dic = {'0':'08', '1':'124', '2':'1235', '3': '236',
    '4':'1457', '5':'24568', '6':'3569', '7':'478', '8':'57890', '9':'689'}
  
  posses = ['']
  
  for e in pincode:
    new_posses = []
    for code in posses:
      for nex in dic[e]:
        new_posses.append(code+nex)
    posses = new_posses
  
  return sorted(posses)

