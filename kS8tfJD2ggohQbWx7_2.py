
def last_name_lensort(names):
  def name_formatter(names):
    tr = {}
    for name in names:
      first, last = name.split()  
      tr[last] = name
    return tr
  def length_sorter(last_names):
    tr = {}
    for name in last_names:
      if len(name) not in tr.keys():
        tr[len(name)] = [name]
      else:
        tr[len(name)].append(name)
    return tr
  
  nf = name_formatter(names)
  ls = length_sorter(list(nf.keys()))
  
  tr = []
  
  for length in sorted(list(ls.keys())):
    if len(ls[length]) > 1:
      nl = sorted(ls[length])
    else:
      nl = ls[length]
    
    for item in nl:
      tr.append(nf[item])
  
  return tr

