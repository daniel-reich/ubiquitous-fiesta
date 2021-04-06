
def num_to_eng(n):
  key = [['zero', 'ten '], 
       ['one', 'eleven '], 
       ['two', 'twen'], 
       ['three', 'thir'], 
       ['four', 'four'], 
       ['five', 'fif'], 
       ['six', 'six'], 
       ['seven', 'seven'], 
       ['eight', 'eigh'], 
       ['nine', 'nine']]
​
  res = []
  hun = n//100 % 10
  ten = n//10 % 10
  uni = n % 10
​
  if hun: 
    res.append(key[hun][0] + ' hundred') 
  if ten > 1: 
    res.append(key[ten][1] + 'ty')
  if ten == 1: 
    res.append((key[uni][1] + 'teen').replace(' teen', '').replace('twenteen', 'twelve'))
  elif uni:
    res.append(key[uni][0])
  
  return key[uni][0] if not res else ' '.join(res)

