
def spartans_cipher(message, n_Slide):
  
  if not message:
    return ""
  arr = [] 
  
  if len(message) % n_Slide == 0:
    horizontal_length = int(len(message) / n_Slide)
  else:
    horizontal_length = len(message) // n_Slide + 1
  
  while message:
    
    temp_holder = [] 
    for i in range(horizontal_length): 
      try:
        temp_holder.append(message[0])
        message = message[1:]
        flag = False
      except Exception as e:
        # Index error 
        # The string is empty 
        temp_holder.append(" ")
        flag = True 
        break
    arr.append(temp_holder)
    if flag and len(arr) != n_Slide: 
      arr.append([" " for i in range(horizontal_length)])
  
  while len(arr[-1]) != horizontal_length:
    arr[-1].append(" ")
    
​
  for i in arr: print(i)
​
  encoded = "" 
  for i in range(horizontal_length):
    for row in arr:
      encoded += row[i]
  
  print()
  print(encoded)
  return(encoded.rstrip())

