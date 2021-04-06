
def split_bunches(bunches):
  def split(bunch):
    name = bunch['name']
    quant = bunch['quantity']
    
    tr = []
    
    for n in range(quant):
      tr.append({'name': name, 'quantity': 1})
    
    return tr
  
  tr = []
  
  for bunch in bunches:
    for dic in split(bunch):
      tr.append(dic)
  
  return tr

