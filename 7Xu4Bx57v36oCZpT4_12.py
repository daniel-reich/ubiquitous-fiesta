
def where_is_waldo(lst):
  locate = differ_char(lst)
  for i in range(0,len(lst)):
    for j in range(0,len(lst[i])):
      if lst[i][j] == locate:
        return [i+1,j+1]
  
​
def differ_char(lst):
  chars ={}
  for ele in lst:
    for char in ele:
      if char in chars:
        chars[char] +=1
      else:
        chars[char] =1
  if len(chars) !=1:
    locate =''
    for key,values in chars.items():
      if chars[key] == 1:
        locate = key
  return locate

