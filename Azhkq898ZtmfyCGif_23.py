
def divide_list(lst, separator):
  if separator not in lst:
    return [lst]
  
  cuts = []
  for i in range(len(lst)):
    if lst[i] == separator:
      cuts.append(i)
  
  sublists = [ lst[0 : cuts[0]] ]
  for c in range(1, len(cuts)):
    sublists.append( lst[ cuts[c-1]+1 : cuts[c] ] )
  sublists.append( lst[ cuts[-1]+1 : ] )
  return sublists   
​
def numbers_to_ranges(lst):
  if lst == []:
    return lst
  divided = [ sorted(lst)[0] ]
  for i in range(1,len(lst)):
    if sorted(lst)[i] == sorted(lst)[i-1] + 1:
      divided.append( sorted(lst)[i] )
    else:
      divided.append( 'x' )
      divided.append( sorted(lst)[i] )
  divided = divide_list(divided, 'x')
  
  output = []
  for sublist in divided:
    if len(sublist) == 1:
      output.append( str(sublist[0]) )
    else:
      output.append( str(sublist[0]) + '-' + str(sublist[-1]) )
  return output

