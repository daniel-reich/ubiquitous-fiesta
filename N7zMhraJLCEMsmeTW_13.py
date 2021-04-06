
def min_swaps(string):
  def return_possible(l):
    
    p1 = ''
    p2 = ''
    
    check = False
    
    for n in range(l):
      
      if check == False:
        p1 += '1'
        p2 += '0'
        
        check = True
      elif check == True:
        p1 += '0'
        p2 += '1'
        
        check = False
    
    return [p1, p2] 
  def swaps(s, poss):
    
    zdif = 0
    odif = 0
    print(s, poss)
    for n in range(len(s)):
      st = s[n]
      pt = poss[n]
      
      if st != pt:
        if st == '0':
          zdif += 1
        elif st == '1':
          odif += 1
        print(st, pt)
    
    return zdif + odif
  
  rp = return_possible(len(string))
  
  p1 = rp[0]
  p2 = rp[1]
  
  p1_str_dif = swaps(string, p1)
  p2_str_dif = swaps(string, p2)
  
  return min([p1_str_dif, p2_str_dif])

