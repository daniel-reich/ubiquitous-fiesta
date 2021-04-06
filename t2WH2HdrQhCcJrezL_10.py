
def eda_bit(start, end):
  result = []
  for i in range(start,end+1):
    
    if i%3 and i%5 : result.append(i)
    
    if not i%3 and not i%5 : result.append("EdaBit")
    
    if (not i%3) and i%5 : result.append("Eda")
  
    if (not i%5) and i%3 : result.append("Bit")
    
    
    print("i = {},result = {}".format(i,result))
    
  return result

