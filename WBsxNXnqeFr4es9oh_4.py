
def square_list(n):
  
  if n==1:
    return [[1]]
  
  elif n==2:
    return [[1,2],[4,3]]
  
  else:
    ans = []
    for i in range(n):
      element = []
      for j in range(n):
        element.append(None)
      ans.append(element)
    
    k = 1
    for i in range(n-1):
      ans[0][i] = k
      k += 4
    
    k = 2
    for i in range(n-1):
      ans[i][n-1] = k
      k += 4
      
    k = 3
    for i in range(-1,-n,-1):
      ans[n-1][i] = k
      k += 4
      
    k = 4
    for i in range(-1,-n,-1):
      ans[i][0] = k
      k += 4
      
    array = square_list(n-2)
    for i in range(n-2):
      for j in range(n-2):
        ans[i+1][j+1] = array[i][j] + 4*n - 4
    return ans
        
def clockwise_cipher(message):
  n = 0
  L = len(message)
  while True:
    if n**2 >= L:
      break
    n += 1
  new_message = message
  while len(new_message)<n**2:
    new_message += " "
  ans = ""
  array = square_list(n)
  for i in range(n):
    for j in range(n):
      ans += new_message[array[i][j]-1]
  return ans

