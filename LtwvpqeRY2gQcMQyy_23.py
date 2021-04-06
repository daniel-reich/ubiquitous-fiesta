
def sig_figs(num):
​
  if float(num) == 0:
    return 0
    
  sig_dig = list('123456789')
  sig_dig_indexes = []
  period_index = None
​
  for n in range(len(num)):
    if num[n] in sig_dig:
      sig_dig_indexes.append(n)
    if num[n] == '.':
      period_index = n
  
  start = min(sig_dig_indexes)
  
  if '.' in num:
    if start < period_index:
      end = len(num) -1
    else:
      end = len(num) 
  else:
    end = max(sig_dig_indexes)+1
  
  return end-start

