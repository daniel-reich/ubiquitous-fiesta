
def get_lucky_number(size, n):   
  iteration = 1
  original_list = list(range(1, size+1))
  survivors = original_list[0 : len(original_list) : 2]     
        
  while len(survivors) > survivors[iteration - 1]:    
    iteration += 1  
    for i in range( survivors[iteration-1], len(survivors), survivors[iteration-1] ):   
      survivors[i-1] = 'x'    
    for char in survivors:
      if char == 'x':
        survivors.remove(char)
  
  return survivors[n-1]

