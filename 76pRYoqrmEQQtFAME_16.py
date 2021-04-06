
def is_astonishing(num):
  a, b = [], []
  AB, BA = [], []
  partition_index = 1
  
  while partition_index < len(str(num)):
    a = int(str(num)[0:partition_index])
    b = int(str(num)[partition_index:])
    partition_index += 1
    
    if int(a) < int(b):  
      if (((a+b)/2)*(b-a+1)) == num:
        AB.append(num)     
    else:  
      
      if (((a+b)/2)*(a-b+1)) == num: 
        BA.append(num)
   
  if num in AB:
    return "AB-Astonishing"
  elif num in BA: 
    return "BA-Astonishing"
  else: 
    return False

