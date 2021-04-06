
def negative_sum(chars):
  chars = chars.replace('%',' ').replace('&',' ').split(' ')
  total = 0
  for eachnum in chars:
    if '-' in eachnum:
      eachnum = eachnum.split('-')
      total += sum(list([int(x)*-1 for x in eachnum if x != '']))
    else:
      continue
  return total
  #return sum(list([int(x) for x in chars if '-' in x]))

