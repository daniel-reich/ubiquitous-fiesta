
def unique(lst):
  for item in lst:
    while lst.count(item) > 1:
      lst.remove(item)
  return lst
  
def clean_up(files, criteria):
  split_files = []
  for f in files:
    split_files.append( f.split('.') )
    
  prefixes = []
  suffixes = []
  subgroup = []
  output = []
  
  for f in split_files:
    prefixes.append(f[0])
    suffixes.append(f[1])
  prefixes = unique(prefixes)
  suffixes = unique(suffixes)
  
  if criteria == 'prefix':
    for p in prefixes:
      for item in split_files:
        if item[0] == p:
          subgroup.append( '.'.join(item) )
      output.append(subgroup)
      subgroup = []
  
  else:
    for s in suffixes:
      for item in split_files:
        if item[1] == s:
          subgroup.append( '.'.join(item) )
      output.append(subgroup)
      subgroup = []
  return output

