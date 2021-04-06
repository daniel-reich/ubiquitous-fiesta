
def num_to_eng(n):
  if n == 0:
    return 'zero'
  ones = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
  tens = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
  teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
        18:'eighteen',19:'nineteen'}
  n_str = str(n)
  lst = []
  for i in range(len(n_str),0,-1):
    index = -1 * i
    num = int(n_str[index])
    if num==0:
      continue
    if index==-3:
      lst.append(ones[num]+' hundred')
    elif index==-2:
      if num == 1:
        num = int(n_str[index]+n_str[index+1])
        lst.append(teens[num])
        break
      else:
        lst.append(tens[num])
    else:
      lst.append(ones[num])
  ans = ' '.join(lst)
  return ans

